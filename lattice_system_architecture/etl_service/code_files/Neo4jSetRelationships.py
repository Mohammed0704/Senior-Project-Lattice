try:
  from code_files.Neo4jConnection import * #docker
except: 
  from Neo4jConnection import * #locally
import pandas as pd
from pandas import json_normalize
from ast import literal_eval
import os

class Neo4jSetRelationships:
  relationsPath = "/resources/relationships.txt"

  def setRelationships(self):
    commands = self.parseFile()
    for cmd in commands:
      Neo4jConnection.query(cmd)
    print("\nRelationships created!")

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
  
  #copies CSVs of logs into import directory in docker (volume, AKA neo4j/import/)
  def importLogFilesAsCSV(self):

    #need to run from code_files folder
    logsPath = '../../../lattice_databases/elasticsearch/data_files/logs/'
    targetPath = '../../neo4j/import/logs/' #path to volume to put the new csvs into

    if not os.path.exists(targetPath):
      os.mkdir(targetPath)

    logFiles = ['LibraryLogs.json', 'RecreationCenterLogs.json', 'SystemsLogs.json']
    targetFiles = ['LibraryLogs.csv', 'RecreationCenterLogs.csv', 'SystemsLogs.csv']

    for i in range(0, len(logFiles)):
      jsonLogs = []
      lineNum = 1
      with open(logsPath + logFiles[i]) as f:
        for line in f.readlines():
          if (lineNum % 2) == 0:
            jsonLogs.append(literal_eval(line.strip('\n'))) #get a dict of line 2, 4, 6, etc. w/o the newline
          lineNum += 1
      df = json_normalize(jsonLogs).set_index('drexelID') #pandas dataframe
      df.to_csv(targetPath + targetFiles[i])

if __name__=="__main__":
  #Imports log file JSONs into CSVs by putting the CSVs into the neo4j/import/ folder (volume)
  myClass = Neo4jSetRelationships()
  myClass.importLogFilesAsCSV()