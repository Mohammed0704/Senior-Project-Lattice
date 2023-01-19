from flask import Flask, render_template, redirect, url_for
app = Flask(__name__, static_folder="static_files", template_folder="static_files/templates")

@app.route('/')
def base():
    return redirect(url_for("home"))

@app.route("/home")
def home():
    return render_template("home_page.html")

@app.route("/connections")
def connections():
    connectionsList = [
        ["testMaria", "MariaDB", "mariaurl:5555", "user"],
        ["testMongo", "MongoDB", "mongourl:1234", "test"],
        ["testes", "Elasticsearch", "esurl:9200", "us"],
        ["testpost", "Postgres", "post:5432", "admin"],
        ["testcass", "Cassandra", "cassurl:9402", "user"]
    ]
    return render_template("menu_template.html") + render_template("portal_data_source_connections.html", connectionsList=connectionsList)

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
    schemaList = ["schema1", "schema1", "schema2"]
    return render_template("menu_template.html") + render_template("data_object_pages/data_object_schemas_page.html", schemaList=schemaList, connectionName=connectionName)

@app.route("/objects/<connectionName>/<schemaName>")
def tables(connectionName, schemaName):
    tableList = ["table1", "table2", "table3"]
    return render_template("menu_template.html") + render_template("data_object_pages/data_object_tables_page.html", tableList=tableList, connectionName=connectionName, schemaName=schemaName)

@app.route("/loader")
def loader():
        return render_template("menu_template.html") + render_template("portal_graph_loader.html")

@app.route("/index")
def index():
    return "index"

@app.route("/about")
def about():
    sites = ['twitter', 'facebook', 'instagram', 'whatsapp']
    return render_template("about.html", sites=sites)

@app.route("/dropdown")
def dropdown():
    colors = ['Red', 'Blue', 'Black', 'Orange']
    return render_template('dropdown.html', colors=colors)

if __name__ == "__main__":
    app.run(host = "0.0.0.0", port = 4999)