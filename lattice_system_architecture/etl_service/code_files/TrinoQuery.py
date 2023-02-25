from abc import ABC, abstractmethod
import pandas as pd

#Strategy interface 
class TrinoQueryStrategy(ABC):
    @abstractmethod
    def query(self, queryTarget, trinoCursor) -> None:
        pass

#Concrete strategies
class TrinoSchemasQuery(TrinoQueryStrategy):
    def query(self, queryTarget, trinoCursor) -> list:
        trinoCursor.execute("SHOW SCHEMAS FROM " + queryTarget)
        rows = trinoCursor.fetchall()

        schemaList = []
        for schema in rows:
            schemaList.append(schema[0])
        return schemaList

class TrinoTablesQuery(TrinoQueryStrategy):
    def query(self, queryTarget, trinoCursor) -> list:
        trinoCursor.execute("SHOW TABLES FROM " + queryTarget)
        rows = trinoCursor.fetchall()

        tableList = []
        for table in rows:
            tableList.append(table[0])
        return tableList

class TrinoColumnsQuery(TrinoQueryStrategy):
    def query(self, queryTarget, trinoCursor) -> list:
        trinoCursor.execute("SHOW COLUMNS FROM " + queryTarget)
        rows = trinoCursor.fetchall()

        columnList = []
        for column in rows:
            columnList.append(column[0])
        return columnList
    
class TrinoSelectQuery(TrinoQueryStrategy):    
    def query(self, queryTarget, trinoCursor):
        trinoCursor.execute(queryTarget)
        rows = trinoCursor.fetchall()
        columns = [column[0] for column in trinoCursor.description]
        queryResult = pd.DataFrame(rows, columns=columns)
        return queryResult

#Context class
class TrinoQuery:
    trinoQueryStrategy: TrinoQueryStrategy

    def __init__(self, trinoQueryStrategy: TrinoQueryStrategy = None) -> None:
        self.trinoQueryStrategy = trinoQueryStrategy

    def executeTrinoQuery(self, queryTarget, trinoCursor):
        return self.trinoQueryStrategy.query(self, queryTarget, trinoCursor)