import trino

#abstracted into its own class so app.py remains clean but still has a single active trino connection
class TrinoConnection:
    trinoCursor = None
    
    @staticmethod
    def establishTrinoConnection():
        trinoConnection = trino.dbapi.connect(
                host="trino", #docker container name #TODO: Abstract this whole section
                port=8080,
                user="trino",
        )
        TrinoConnection.trinoCursor = trinoConnection.cursor() #what is being used to send queries to Trino

    @staticmethod
    def getActiveTrinoCursor():
        if TrinoConnection.trinoCursor is None:
            TrinoConnection.establishTrinoConnection()
        return TrinoConnection.trinoCursor