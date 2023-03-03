from neo4j import GraphDatabase

class Neo4jConnection:
    neo4jSession = None
    neo4jDriver = None

    @staticmethod
    def establishNeo4jConnection():
        # Establishing a connection to Neo4j
        uri = "neo4j://neo4j:7687" #set to the container name
        Neo4jConnection.neo4jDriver = GraphDatabase.driver(uri, auth=("neo4j", "password"))
        Neo4jConnection.neo4jSession = Neo4jConnection.neo4jDriver.session()

    @staticmethod
    def getActiveNeo4jSession():
        if Neo4jConnection.neo4jSession is None:
            Neo4jConnection.establishNeo4jConnection()
        return Neo4jConnection.neo4jSession

    @staticmethod
    def query(query):
        try: #attempt the query; if it fails, close the connection so it isn't left open
            Neo4jConnection.getActiveNeo4jSession().run(query)
        except Exception as e:
            Neo4jConnection.closeConnection()
            print(e)
        
        # Ingesting test data
        #self.session.run("CREATE (:Person {name: 'Test'})-[:KNOWS]->(:Person {name: 'Test2'})")
        #self.session.run("CREATE (:Student {name: 'John'})-[:MANAGES]->(:Person {name: 'Test'})")
        # At this point data can be viewed in the Neo4j browser via http://localhost:7474/browser/
        # Enter "neo4j" for the username and "password" for the password, and click "Connect"

    @staticmethod
    def closeConnection():
        # Closing the session and driver
        if Neo4jConnection.neo4jSession is not None and Neo4jConnection.neo4jDriver is not None:
            Neo4jConnection.neo4jSession.close()
            Neo4jConnection.neo4jDriver.close()
            Neo4jConnection.neo4jSession = None
            Neo4jConnection.neo4jDriver = None
