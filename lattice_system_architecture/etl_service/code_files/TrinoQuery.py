from abc import ABC, abstractmethod
import trino

#Strategy interface 
class QueryTrinoStrategy(ABC):
    trinoConnection = trino.dbapi.connect(
            host="localhost",
            port=8080,
            user="trino",
    )

    trinoCursor = trinoConnection.cursor() #what is being used to send queries to Trino

    @abstractmethod
    def query(self) -> None:
        pass

#Concrete strategies
class QueryTrinoForSchemas(QueryTrinoStrategy):
    def query(self) -> list:
        return ["schema5", "schema6", "schema7"]

class QueryTrinoForTables(QueryTrinoStrategy):
    def query(self) -> list:
        return ["table1", "table2"]

class QueryTrinoForColumns(QueryTrinoStrategy):
    def query(self) -> list:
        return ["column1", "column3", "column3", "column4", "column5", "column6", "column7", "column8", "column9"]

#Context class
class TrinoQuery:
    queryTrinoStrategy: QueryTrinoStrategy

    def __init__(self, queryTrinoStrategy: QueryTrinoStrategy = None) -> None:
        self.queryTrinoStrategy = queryTrinoStrategy

    def executeTrinoQuery(self) -> list:
        return self.queryTrinoStrategy.query(self)