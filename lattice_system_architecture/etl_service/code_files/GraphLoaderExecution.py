from abc import ABC, abstractmethod
import pandas as pd
import os
try:
    from code_files.Serialization import *
    from code_files.SQLGeneration import *
    from code_files.TrinoConnection import *
    from code_files.QueryToCSV import *
    from code_files.Neo4jConnection import *
    from code_files.CypherGeneration import *
    from code_files.Neo4jSetRelationships import *
    from code_files.TrinoQuery import *
except:
    from Serialization import *
    from SQLGeneration import *
    from TrinoConnection import *
    from QueryToCSV import *
    from Neo4jConnection import *
    from CypherGeneration import *
    from Neo4jSetRelationships import *
    from TrinoQuery import *

#Strategy interface 
class GraphLoaderExecutionStrategy(ABC):
    @abstractmethod
    def execute(self) -> None:
        pass

#Concrete strategies
class CSVExecution(GraphLoaderExecutionStrategy):
    def execute(self) -> str:
        tagsDict = Serialization.Deserialize("/serialized_data/SerializedTags.txt")
        sqlGeneration = SQLGeneration()
        queryToCSV = QueryToCSV()

        #removes old data object CSVs
        for oldDataObjectFile in os.listdir(os.environ["import_directory"]):
            os.remove(os.environ["import_directory"] + oldDataObjectFile)

        #generates a data object CSV for each utilized tag
        time = None #time is currently not utilized in the final name of the resulting CSVs TODO: Update this comment when this changes
        for tag in tagsDict:
            taggedColumnsAsSQL = sqlGeneration.generateQuery(tag, tagsDict)
            if taggedColumnsAsSQL is not None: #if there are columns with the current tag applied and isn't a non-base (.join, .concat, etc...) tag
                queryResultDataframe = TrinoConnection.query(TrinoSelectQuery, taggedColumnsAsSQL)
                time = queryToCSV.writeQueryToCSV(tag, queryResultDataframe, time) #update time
        
        return "Tag data updated!"

class ClearExecution(GraphLoaderExecutionStrategy):
    def execute(self) -> str:
        #clear previous data out of Neo4j
        Neo4jConnection.clearAllData()
        return "Previous Neo4j data cleared!"

class NodeCreationExecution(GraphLoaderExecutionStrategy):
    def execute(self) -> str:
        cypherGeneration = CypherGeneration()

        #generate and send query to Neo4j for each data object CSV
        for dataObjectFile in os.listdir(os.environ["import_directory"]):
            dataObjectFileName = os.fsdecode(dataObjectFile)
            cypherCreateQuery = cypherGeneration.generateCypherCreate(dataObjectFileName)
            Neo4jConnection.query(cypherCreateQuery)
        
        return "Neo4j nodes created!"
    
class RelationshipCreationExecution(GraphLoaderExecutionStrategy):
    def execute(self) -> str:
        #create relationships based on text file
        Neo4jSetRelationships().setRelationships()
        return "Neo4j relationships created!"
    
class Neo4jLinkExecution(GraphLoaderExecutionStrategy):
    def execute(self) -> str:
        return "Completed! Access Neo4j at <a id=\"neo4j-link\" href=\"#\" onClick=\"window.open('http://localhost:7474/browser', '_blank')\">http://localhost:7474/browser</a>" #href link should be abstracted and not hardcoded in javascript
    
class Neo4jCloseExecution(GraphLoaderExecutionStrategy):
    def execute(self) -> str:
        Neo4jConnection.closeConnection()
        return "END_OF_EXECUTION"

#Context class
class GraphLoaderExecution:
    graphLoaderExecutionStrategy: GraphLoaderExecutionStrategy

    def __init__(self, graphLoaderExecutionStrategy: GraphLoaderExecutionStrategy = None) -> None:
        self.graphLoaderExecutionStrategy = graphLoaderExecutionStrategy

    def execute(self):
        return self.graphLoaderExecutionStrategy.execute(self)