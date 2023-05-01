import trino
import os

try:
    from code_files.TrinoQuery import *
except:
    from TrinoQuery import *

#abstracted into its own class so app.py remains clean but still has a single active trino connection
class TrinoConnection:
    trinoCursor = None
    
    @staticmethod
    def establishTrinoConnection():
        trinoConnection = trino.dbapi.connect(
                host=os.environ["trino_host"],
                port=os.environ["trino_port"],
                user=os.environ["trino_user"],
        )
        TrinoConnection.trinoCursor = trinoConnection.cursor() #what is being used to send queries to Trino

    @staticmethod
    def getActiveTrinoCursor():
        if TrinoConnection.trinoCursor is None:
            TrinoConnection.establishTrinoConnection()
        return TrinoConnection.trinoCursor
    
    @staticmethod
    def query(trinoQueryStrategy: TrinoQueryStrategy, queryTarget):
        trinoCursor = TrinoConnection.getActiveTrinoCursor()
        return TrinoQuery(trinoQueryStrategy).executeTrinoQuery(queryTarget, trinoCursor)
        