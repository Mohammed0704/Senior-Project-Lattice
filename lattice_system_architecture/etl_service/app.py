from flask import Flask, render_template, redirect, url_for
app = Flask(__name__, static_folder="static_files", template_folder="static_files/templates")

import sys # Temp

sys.path.insert(0, "/code_files")

from Serialization import *
from TrinoConnection import *
from TrinoQuery import *

trinoCursor = None

@app.route('/')
def base():
    return redirect(url_for("home"))

@app.route("/home")
def home():
    return render_template("home_page.html")

@app.route("/connections")
def connections():
    connectionsList = Deserialize("/serialized_data/SerializedConnections.txt")
    return render_template("menu_template.html") + render_template("portal_data_source_connections.html", connectionsList=connectionsList)

@app.route("/connections/remove/<connectionToDelete>", methods=['DELETE'])
def connectionsRemove(connectionToDelete):
    connectionsList = Deserialize("/serialized_data/SerializedConnections.txt")
    for i in range(len(connectionsList)):
        connection = connectionsList[i]
        if connection["connection_name"] == connectionToDelete:
            connectionsList.pop(i)
            break
    Serialize(connectionsList, "/serialized_data/SerializedConnections.txt")
    return "Connection " + connectionToDelete + " removed!"

@app.route("/tags")
def tags():
    tagList = ["Student", "Student.join", "Housing", "System", "Departments", "Colleges", "Employees", "Program", "Area of Study"]
    return render_template("menu_template.html") + render_template("portal_tag_management.html", tagList=tagList)

@app.route("/objects")
def objects():
    connectionList = Deserialize("/serialized_data/SerializedConnections.txt")
    return render_template("menu_template.html") + render_template("data_object_pages/portal_data_object_management.html", connectionList=connectionList)

@app.route("/objects/<connectionName>")
def schemas(connectionName):
    trinoQueryObject = TrinoQuery(QueryTrinoForSchemas)
    schemaList = trinoQueryObject.executeTrinoQuery(connectionName, TrinoConnection.getActiveTrinoCursor())
    return render_template("menu_template.html") + render_template("data_object_pages/data_object_schemas_page.html", schemaList=schemaList, connectionName=connectionName)

@app.route("/objects/<connectionName>/<schemaName>")
def tables(connectionName, schemaName):
    trinoQueryObject = TrinoQuery(QueryTrinoForTables)
    tableList = trinoQueryObject.executeTrinoQuery(connectionName + "." + schemaName, TrinoConnection.getActiveTrinoCursor())
    return render_template("menu_template.html") + render_template("data_object_pages/data_object_tables_page.html", tableList=tableList, connectionName=connectionName, schemaName=schemaName)

@app.route("/objects/<connectionName>/<schemaName>/<tableName>")
def columns(connectionName, schemaName, tableName):
    tablePath = connectionName + "." + schemaName + "." + tableName
    #Maybe make a list of all available tags (ones not on already) on a column
    tagList = ["Student", "Student.join", "Housing", "System", "Departments", "Colleges", "Employees", "Program", "Area of Study"]
    columnTagDict = []
    try:
        columnTagDict = Deserialize("/serialized_data/SerializedTaggedColumns.txt")[tablePath]
    except:
        pass
    trinoQueryObject = TrinoQuery(QueryTrinoForColumns)
    columnList = trinoQueryObject.executeTrinoQuery(tablePath, TrinoConnection.getActiveTrinoCursor())
    return render_template("menu_template.html") + render_template("data_object_pages/data_object_columns_page.html", columnList=columnList, connectionName=connectionName, schemaName=schemaName, tableName=tableName, columnTagDict=columnTagDict, tagList=tagList)

@app.route("/objects/<connectionName>/<schemaName>/<tableName>/<columnName>/add/<tagToAdd>", methods=['POST'])
def addTagToColumn(connectionName, schemaName, tableName, columnName, tagToAdd):
    tablePath = connectionName + "." + schemaName + "." + tableName
    columnTagDict = Deserialize("/serialized_data/SerializedTaggedColumns.txt")
    
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
    Serialize(columnTagDict, "/serialized_data/SerializedTaggedColumns.txt")
    return "Tag " + tagToAdd + " added!"

@app.route("/objects/<connectionName>/<schemaName>/<tableName>/<columnName>/remove/<tagToRemove>", methods=['DELETE'])
def removeTagFromColumn(connectionName, schemaName, tableName, columnName, tagToRemove):
    tablePath = connectionName + "." + schemaName + "." + tableName
    columnTagDict = Deserialize("/serialized_data/SerializedTaggedColumns.txt")
    columnTagList = columnTagDict[tablePath][columnName]
    if len(columnTagList) == 1: #if there are no tags in the list of the current column and/or column, removes the entries
        del columnTagDict[tablePath][columnName]
        if len(columnTagDict[tablePath]) == 0:
            del columnTagDict[tablePath]
    else:
        columnTagList.remove(tagToRemove)
        columnTagDict[tablePath][columnName] = columnTagList
    Serialize(columnTagDict, "/serialized_data/SerializedTaggedColumns.txt")
    return "Tag " + tagToRemove + " removed!"

@app.route("/loader")
def loader():
        return render_template("menu_template.html") + render_template("portal_graph_loader.html")

if __name__ == "__main__":
    app.run(host = "0.0.0.0", port = 4999)