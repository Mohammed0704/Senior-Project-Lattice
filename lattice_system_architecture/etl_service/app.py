from flask import Flask, render_template, redirect, url_for, request, jsonify

app = Flask(__name__, static_folder="static_files", template_folder="static_files/templates")

from code_files.Serialization import *
from code_files.TrinoConnection import *
from code_files.TrinoConnectors import *
from code_files.Neo4jConnection import *
from code_files.GenerateSQL import *
from code_files.QueryToCSV import *

@app.route('/')
def base():
    return redirect(url_for("home"))

@app.route("/home")
def home():
    return render_template("home_page.html")

@app.route("/connections")
def connections():
    connectionsList = Serialization.Deserialize("/serialized_data/SerializedConnections.txt")
    return render_template("menu_template.html") + render_template("portal_data_source_connections.html", connectionsList=connectionsList)

@app.route("/connections/remove/<connectionToDelete>", methods=['DELETE'])
def connectionsRemove(connectionToDelete):
    connectionsList = Serialization.Deserialize("/serialized_data/SerializedConnections.txt")
    for i in range(len(connectionsList)):
        connection = connectionsList[i]
        if connection["connection_name"] == connectionToDelete:
            connectionsList.pop(i)
            break
    Serialization.Serialize(connectionsList, "/serialized_data/SerializedConnections.txt")
    return "Connection " + connectionToDelete + " removed!"

# create-new-page
@app.route("/connections/create", methods=["GET", "POST"])
def connections_create():
    '''
    if (exists('./serialized_data/SerializedConnections.txt')):
        with open('./serialized_data/SerializedConnections.txt', 'r') as listConns:
            currConns = literal_eval(listConns)
    else:
        currConns = []
    '''
    # Don't need a route for submitting the form, it automatically sends it back to this route with the post method
    
    currConns = Serialization.Deserialize("/serialized_data/SerializedConnections.txt")
    databaseTypes = ["Cassandra", "Elasticsearch", "Postgres", "MariaDB", "MongoDB"]
    if request.method == "POST":
        data = request.form
        newConn = {
            'connection_name': data['name'],
            'connection_type': data['data_source'],
            'connection_URL': data['address'] + ':' + data['port'],
            'connection_username': data['username'],
            'connection_password': data['password']
        }
        currConns.append(newConn)
        
        Serialization.Serialize(currConns, "/serialized_data/SerializedConnections.txt")
        trinoConnectorCreator = TrinoConnector()
        trinoConnectorCreator.createConnector(newConn)
    
    return render_template("menu_template.html") + render_template("portal_data_source_connections_create.html", databaseTypes=databaseTypes)   
    

@app.route("/tags")
def tags():
    tagDict = Serialization.Deserialize('serialized_data/SerializedTags.txt')
    return render_template("menu_template.html") + render_template("portal_tag_management.html", tagDict=tagDict)

@app.route("/tags/create")
def tags_create():
    return render_template("menu_template.html") + render_template("portal_create_new_tag.html")

@app.route('/tags/create/create-tag', methods=['POST'])
def create_tag():
    # Extract JSON payload from request
    tagDict = request.get_json()
    tagName = tagDict.get("tag_name")
    filePath = "serialized_data/SerializedTags.txt"

    if not tagName or " " in tagName:
        return jsonify({"success": False, "message": "Cannot have spaces in the name"})

    # Load existing tags from file
    tagsDict = Serialization.Deserialize(filePath)

    # If the tag already exists, return an error message
    if tagName in tagsDict.keys():
        return jsonify({"success": False, "message": "Tag already exists"})

    # If the tag does not exist, write the new tag to the file
    with open(filePath, 'w') as f:
        tagsDict[tagName] = {"columns_tagged": []}
        sortedTagsDict = {key: val for key, val in sorted(tagsDict.items(), key = lambda ele: ele[0])} #alphabetizes tags
        Serialization.Serialize(sortedTagsDict, "serialized_data/SerializedTags.txt")

    return jsonify({"success": True, "message": "Tag was added"})

@app.route("/tags/remove/<tagToDelete>", methods=['DELETE'])
def tagsRemove(tagToDelete):
    filePath = "serialized_data/SerializedTags.txt"
    tagsDict = Serialization.Deserialize(filePath)
    
    # removes the tag from the list of created tags
    del tagsDict[tagToDelete]
    
    # checks if tagToDelete is also in SerializedTaggedColumns.txt and removes from there as well
    columnTagDict = Serialization.Deserialize("/serialized_data/SerializedTaggedColumns.txt")
    for tablePath in columnTagDict:
        for columnName in columnTagDict[tablePath]:
            if tagToDelete in columnTagDict[tablePath][columnName]:
                connectionName, schemaName, tableName = tablePath.split(".")
                removeTagFromColumn(connectionName, schemaName, tableName, columnName, tagToDelete)
    
    sortedTagsDict = {key: val for key, val in sorted(tagsDict.items(), key = lambda ele: ele[0])} #alphabetizes tags
    Serialization.Serialize(sortedTagsDict, filePath)
    return "Tag " + tagToDelete + " removed!"

@app.route("/objects")
def objects():
    connectionList = Serialization.Deserialize("/serialized_data/SerializedConnections.txt")
    return render_template("menu_template.html") + render_template("data_object_pages/portal_data_object_management.html", connectionList=connectionList)

@app.route("/objects/<connectionName>")
def schemas(connectionName):
    schemaList = TrinoConnection.query(QueryTrinoForSchemas, connectionName)
    return render_template("menu_template.html") + render_template("data_object_pages/data_object_schemas_page.html", schemaList=schemaList, connectionName=connectionName)

@app.route("/objects/<connectionName>/<schemaName>")
def tables(connectionName, schemaName):
    tableList = TrinoConnection.query(QueryTrinoForTables, connectionName + "." + schemaName)
    return render_template("menu_template.html") + render_template("data_object_pages/data_object_tables_page.html", tableList=tableList, connectionName=connectionName, schemaName=schemaName)

@app.route("/objects/<connectionName>/<schemaName>/<tableName>")
def columns(connectionName, schemaName, tableName):
    tablePath = connectionName + "." + schemaName + "." + tableName
    #Maybe make a list of all available tags (ones not on already) on a column
    tagDict = Serialization.Deserialize('serialized_data/SerializedTags.txt')
    columnTagDict = []
    try:
        columnTagDict = Serialization.Deserialize("/serialized_data/SerializedTaggedColumns.txt")[tablePath]
    except:
        pass
    columnList = TrinoConnection.query(QueryTrinoForColumns, connectionName + "." + schemaName + "." + tableName)
    return render_template("menu_template.html") + render_template("data_object_pages/data_object_columns_page.html", columnList=columnList, connectionName=connectionName, schemaName=schemaName, tableName=tableName, columnTagDict=columnTagDict, tagDict=tagDict)

@app.route("/objects/<connectionName>/<schemaName>/<tableName>/<columnName>/add/<tagToAdd>", methods=['POST'])
def addTagToColumn(connectionName, schemaName, tableName, columnName, tagToAdd):
    tablePath = connectionName + "." + schemaName + "." + tableName
    columnTagDict = Serialization.Deserialize("/serialized_data/SerializedTaggedColumns.txt")
    tagsDict = Serialization.Deserialize("serialized_data/SerializedTags.txt")
    
    #adds the tag based on whether new dictionary entries need to be made or not
    if tablePath in columnTagDict.keys():
        tableDict = columnTagDict[tablePath]
        if columnName in tableDict.keys():
            columnTagList = tableDict[columnName]
            columnTagList.append(tagToAdd)
            tableDict[columnName] = columnTagList
        else:
            tableDict[columnName] = [tagToAdd]
        columnTagDict[tablePath] = tableDict
    else:
        columnTagDict[tablePath] = {columnName: [tagToAdd]}

    #updates the tag'sassociated tagged columns
    taggedColumnsForTagList = tagsDict[tagToAdd]["columns_tagged"]
    taggedColumnsForTagList.append(tablePath + "." + columnName)
    tagsDict[tagToAdd]["columns_tagged"] = taggedColumnsForTagList

    Serialization.Serialize(columnTagDict, "/serialized_data/SerializedTaggedColumns.txt")
    Serialization.Serialize(tagsDict, "serialized_data/SerializedTags.txt")
    return "Tag " + tagToAdd + " added!"

@app.route("/objects/<connectionName>/<schemaName>/<tableName>/<columnName>/remove/<tagToRemove>", methods=['DELETE'])
def removeTagFromColumn(connectionName, schemaName, tableName, columnName, tagToRemove):
    tablePath = connectionName + "." + schemaName + "." + tableName
    columnTagDict = Serialization.Deserialize("/serialized_data/SerializedTaggedColumns.txt")
    columnTagList = columnTagDict[tablePath][columnName]
    tagsDict = Serialization.Deserialize("serialized_data/SerializedTags.txt")

    if len(columnTagList) == 1: #if there are no tags in the list of the current column and/or column, removes the entries
        del columnTagDict[tablePath][columnName]
        if len(columnTagDict[tablePath]) == 0:
            del columnTagDict[tablePath]
    else:
        columnTagList.remove(tagToRemove)
        columnTagDict[tablePath][columnName] = columnTagList

    #updates the tag'sassociated tagged columns
    taggedColumnsForTagList = tagsDict[tagToRemove]["columns_tagged"]
    taggedColumnsForTagList.remove(tablePath + "." + columnName)
    tagsDict[tagToRemove]["columns_tagged"] = taggedColumnsForTagList

    Serialization.Serialize(columnTagDict, "/serialized_data/SerializedTaggedColumns.txt")
    Serialization.Serialize(tagsDict, "serialized_data/SerializedTags.txt")
    return "Tag " + tagToRemove + " removed!"

@app.route("/loader")
def loader():
    generateSQL = GenerateSQL()
    queryToCSV = QueryToCSV()
    tagsDict = Serialization.Deserialize("/serialized_data/SerializedTags.txt")

    time = None #time is currently not utilized in the final name of the resulting CSVs
    for tag in tagsDict:
        taggedColumnsAsSQL = generateSQL.generateQuery(tag, tagsDict)
        if taggedColumnsAsSQL is not None:
            queryResultDataframe = TrinoConnection.query(QueryTrinoWithSelect, taggedColumnsAsSQL)
            time = queryToCSV.writeQueryToCSV(tag, queryResultDataframe, time)
        
    return render_template("menu_template.html") + render_template("portal_graph_loader.html")

if __name__ == "__main__":
    app.run(host = "0.0.0.0", port = 4999)