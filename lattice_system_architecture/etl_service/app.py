from flask import Flask, render_template, redirect, url_for
app = Flask(__name__, static_folder="static_files", template_folder="static_files/templates")

import os
''' If we want to put the code files back in their own directory
import sys
sys.path.append(f"{os.getcwd()}{os.sep}code_files")
'''
from Serialization import Serialize, Deserialize

dir_path = os.path.dirname(os.path.realpath(__file__))

@app.route('/')
def base():
    return redirect(url_for("home"))

@app.route("/home")
def home():
    return render_template("home_page.html")

@app.route("/connections")
def connections():
    connectionsList = Deserialize(f"{dir_path}{os.sep}serialized_data{os.sep}SerializedConnections.txt")
    return render_template("menu_template.html") + render_template("portal_data_source_connections.html", connectionsList=connectionsList)

@app.route("/connections/remove/<connectionToDelete>", methods=['DELETE'])
def connectionsRemove(connectionToDelete):
    #data = request.args.get("jsdata")
    with open('serialized_data/this_is_a_test.txt', 'w') as f:
        json.dump("Last connection deleted: " + connectionToDelete, f)
    return "Connection " + connectionToDelete + " removed!"

@app.route("/tags")
def tags():
    tagList = ["Student", "Housing", "System", "Departments", "Colleges", "Employees", "Program", "Area of Study"]
    return render_template("menu_template.html") + render_template("portal_tag_management.html", tagList=tagList)

@app.route("/objects")
def objects():
    connectionList = ["MDB - MariaDB", "MonDB - MongoDB", "ES - Elasticsearch", "ES - Elasticsearch", "ES - Elasticsearch", "ES - Elasticsearch", "testing"]
    return render_template("menu_template.html") + render_template("data_object_pages/portal_data_object_management.html", connectionList=connectionList)

@app.route("/objects/<connectionName>")
def schemas(connectionName):
    schemaList = ["schema1", "schema2"]
    return render_template("menu_template.html") + render_template("data_object_pages/data_object_schemas_page.html", schemaList=schemaList, connectionName=connectionName)

@app.route("/objects/<connectionName>/<schemaName>")
def tables(connectionName, schemaName):
    tableList = ["table1", "table2", "table3"]
    return render_template("menu_template.html") + render_template("data_object_pages/data_object_tables_page.html", tableList=tableList, connectionName=connectionName, schemaName=schemaName)

@app.route("/objects/<connectionName>/<schemaName>/<tableName>")
def columns(connectionName, schemaName, tableName):
    columnList = ["column1", "column3", "column3", "column4", "column5", "column6", "column7", "column8", "column9"]
    return render_template("menu_template.html") + render_template("data_object_pages/data_object_columns_page.html", columnList=columnList, connectionName=connectionName, schemaName=schemaName, tableName=tableName)

@app.route("/loader")
def loader():
        return render_template("menu_template.html") + render_template("portal_graph_loader.html")

if __name__ == "__main__":
    app.run(host = "0.0.0.0", port = 4999)