from neo4j import GraphDatabase
import Neo4jConnection

class Neo4jSetRelationships:
    session = Neo4jConnection.getActiveNeo4jSession()
    driver = GraphDatabase.driver("neo4j://neo4j:7687", auth=("neo4j", "password"))

    @staticmethod
    def setRelationships():
      