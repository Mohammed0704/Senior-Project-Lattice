from neo4j import GraphDatabase

class Neo4jConnection:
    session = None
    driver = None

    def __init__(self):
        self.establishNeo4jConnection()

    def establishNeo4jConnection(self):
        # Establishing a connection to Neo4j
        uri = "neo4j://neo4j:7687" #set to the container name
        driver = GraphDatabase.driver(uri, auth=("neo4j", "password"))
        self.session = driver.session()

    def query(self):
        # Ingesting data
        self.session.run("CREATE (:Person {name: 'Test'})-[:KNOWS]->(:Person {name: 'Test2'})")
        self.session.run("CREATE (:Student {name: 'John'})-[:MANAGES]->(:Person {name: 'Test'})")
        # At this point data can be viewed in the Neo4j browser via http://localhost:7474/browser/
        # Enter "neo4j" for the username and "password" for the password, and click "Connect"

    def closeConnection(self):
        # Closing the session and driver
        self.session.close()
        self.driver.close()
