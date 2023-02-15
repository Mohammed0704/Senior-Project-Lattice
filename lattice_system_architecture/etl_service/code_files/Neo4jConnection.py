from neo4j import GraphDatabase

class Neo4jConnection:
    def establishNeo4jConnection():
    # Establishing a connection to Neo4j
        uri = "neo4j://localhost:7687"
        driver = GraphDatabase.driver(uri, auth=("neo4j", "passtest"))
        session = driver.session()

    # Ingesting data
        session.run("CREATE (:Person {name: 'Test'})-[:KNOWS]->(:Person {name: 'Test2'})")
        session.run("CREATE (:Student {name: 'John'})-[:MANAGES]->(:Person {name: 'Test'})")

    # At this point data can be viewed in the Neo4j browser via http://localhost:7474/browser/
    # Enter "neo4j" for the username and "passtest" for the password, and click "Connect"

    # Closing the session and driver
        session.close()
        driver.close()

    if __name__ == "__main__":
        establishNeo4jConnection()
