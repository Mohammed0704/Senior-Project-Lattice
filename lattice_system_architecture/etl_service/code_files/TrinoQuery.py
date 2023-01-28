from abc import ABC, abstractmethod
#import pandas as pd

#Strategy interface 
class QueryTrinoStrategy(ABC):
    @abstractmethod
    def query(self, queryTarget, trinoCursor) -> None:
        pass

#Concrete strategies
class QueryTrinoForSchemas(QueryTrinoStrategy):
    def query(self, queryTarget, trinoCursor) -> list:
        trinoCursor.execute("SHOW SCHEMAS FROM " + queryTarget)
        rows = trinoCursor.fetchall()

        schemaList = []
        for schema in rows:
            schemaList.append(schema[0])
        return schemaList

class QueryTrinoForTables(QueryTrinoStrategy):
    def query(self, queryTarget, trinoCursor) -> list:
        return ["table1", "table2"]

class QueryTrinoForColumns(QueryTrinoStrategy):
    def query(self, queryTarget, trinoCursor) -> list:
        return ["column1", "column3", "column3", "column4", "column5", "column6", "column7", "column8", "column9"]

#Context class
class TrinoQuery:
    queryTrinoStrategy: QueryTrinoStrategy

    def __init__(self, queryTrinoStrategy: QueryTrinoStrategy = None) -> None:
        self.queryTrinoStrategy = queryTrinoStrategy

    def executeTrinoQuery(self, queryTarget, trinoCursor) -> list:
        return self.queryTrinoStrategy.query(self, queryTarget, trinoCursor)