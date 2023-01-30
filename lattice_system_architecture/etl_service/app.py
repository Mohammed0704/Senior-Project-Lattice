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
    tagList = ["Student", "Student.join", "Housing", "System", "Departments", "Colleges", "Employees", "Program", "Area of Study"]
    trinoQueryObject = TrinoQuery(QueryTrinoForColumns)
    columnList = trinoQueryObject.executeTrinoQuery(connectionName + "." + schemaName + "." + tableName, TrinoConnection.getActiveTrinoCursor())
    return render_template("menu_template.html") + render_template("data_object_pages/data_object_columns_page.html", columnList=columnList, connectionName=connectionName, schemaName=schemaName, tableName=tableName, tagList=tagList)

@app.route("/loader")
def loader():
        return render_template("menu_template.html") + render_template("portal_graph_loader.html")

if __name__ == "__main__":
    app.run(host = "0.0.0.0", port = 4999)