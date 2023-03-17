from code_files.Neo4jConnection import *

class Neo4jSetRelationships:
  session = Neo4jConnection.getActiveNeo4jSession()
  relationsPath = "/resources/relationships.txt"

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
          s += line
        else:
          cmds.append(s)
          s = ""
    return cmds