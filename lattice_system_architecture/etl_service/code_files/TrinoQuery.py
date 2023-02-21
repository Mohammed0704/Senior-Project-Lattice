from abc import ABC, abstractmethod
import pandas as pd

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
        trinoCursor.execute("SHOW TABLES FROM " + queryTarget)
        rows = trinoCursor.fetchall()

        tableList = []
        for table in rows:
            tableList.append(table[0])
        return tableList

class QueryTrinoForColumns(QueryTrinoStrategy):
    def query(self, queryTarget, trinoCursor) -> list:
        trinoCursor.execute("SHOW COLUMNS FROM " + queryTarget)
        rows = trinoCursor.fetchall()

        columnList = []
        for column in rows:
            columnList.append(column[0])
        return columnList
    
class QueryTrinoWithSelect(QueryTrinoStrategy):    
    def query(self, queryTarget, trinoCursor):
        trinoCursor.execute(queryTarget)
        rows = trinoCursor.fetchall()
        columns = [column[0] for column in trinoCursor.description]
        queryResult = pd.DataFrame(rows, columns=columns)
        return queryResult

#Context class
class TrinoQuery:
    queryTrinoStrategy: QueryTrinoStrategy

    def __init__(self, queryTrinoStrategy: QueryTrinoStrategy = None) -> None:
        self.queryTrinoStrategy = queryTrinoStrategy

    def executeTrinoQuery(self, queryTarget, trinoCursor):
        return self.queryTrinoStrategy.query(self, queryTarget, trinoCursor)