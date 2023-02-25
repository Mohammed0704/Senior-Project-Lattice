from neo4j import GraphDatabase
import Neo4jConnection

class Neo4jSetRelationships:
    session = Neo4jConnection.getActiveNeo4jSession()
    driver = GraphDatabase.driver("neo4j://neo4j:7687")#, auth=("neo4j", "password"))
    relationsPath = "../resources/relationships.txt"

    def setRelationships(self):
      commands = self.parseFile()
      for cmd in commands:
        self.session.run(cmd)

    def parseFile(self):
      s = ""
      cmds= []
      with open(self.relationsPath, "r") as f:
        for line in f.readlines():
          if line.rstrip("\n") != "//:":
            s.append(line)
          else:
            cmds.append(s)
            s = ""
      return cmds