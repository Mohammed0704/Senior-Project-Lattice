import trino

#abstracted into its own class so app.py remains clean but still has a single active trino connection
class EstablishTrinoConnection:
    trinoCursor = None
    
    @staticmethod
    def establishTrinoConnection():
        trinoConnection = trino.dbapi.connect(
                host="trino", #docker container name #TODO: Abstract this whole section
                port=8080,
                user="trino",
        )
        print("cursor created")
        EstablishTrinoConnection.trinoCursor = trinoConnection.cursor() #what is being used to send queries to Trino

    @staticmethod
    def getActiveTrinoCursor():
        if EstablishTrinoConnection.trinoCursor is None:
            EstablishTrinoConnection.establishTrinoConnection()
        return EstablishTrinoConnection.trinoCursor