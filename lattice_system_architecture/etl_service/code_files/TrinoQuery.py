from abc import ABC, abstractmethod
import trino
#import pandas as pd

#Strategy interface 
class QueryTrinoStrategy(ABC):
    @abstractmethod
    def query(self, queryTarget) -> None:
        pass

#Concrete strategies
class QueryTrinoForSchemas(QueryTrinoStrategy):
    def query(self, queryTarget) -> list:
        self.trinoCursor.execute("SHOW SCHEMAS FROM " + queryTarget)
        rows = self.trinoCursor.fetchall()

        schemaList = []
        for schema in rows:
            schemaList.append(schema[0])
        return schemaList

class QueryTrinoForTables(QueryTrinoStrategy):
    def query(self, queryTarget) -> list:
        return ["table1", "table2"]

class QueryTrinoForColumns(QueryTrinoStrategy):
    def query(self, queryTarget) -> list:
        return ["column1", "column3", "column3", "column4", "column5", "column6", "column7", "column8", "column9"]

#Context class
class TrinoQuery:
    queryTrinoStrategy: QueryTrinoStrategy
    trinoCursor = None

    def __init__(self, queryTrinoStrategy: QueryTrinoStrategy = None) -> None:
        self.queryTrinoStrategy = queryTrinoStrategy

    def executeTrinoQuery(self, queryTarget) -> list:
        self.establishTrinoConnection()
        return self.queryTrinoStrategy.query(self, queryTarget)

    def establishTrinoConnection(self):
        trinoConnection = trino.dbapi.connect(
                host="trino",
                port=8080,
                user="trino",
        )
        self.trinoCursor = trinoConnection.cursor() #what is being used to send queries to Trino
