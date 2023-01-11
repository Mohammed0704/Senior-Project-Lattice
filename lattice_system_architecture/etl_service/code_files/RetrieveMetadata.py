import trino
import pandas as pd

class RetrieveMetadata:
    trinoCursor = None
    trinoHost = "localhost"
    trinoPort = 8080
    trinoUser = "user"

    def __init__(self):
        pass

    def ConnectToTrino(self):
        trinoConnection = trino.dbapi.connect(
            host=self.trinoHost,
            port=self.trinoPort,
            user=self.trinoUser
        )
        self.trinoCursor = trinoConnection.cursor() #what is being used to send queries to Trino

    #Trino has a query sent to it and the results are stored in a Pandas dataframe
    def RetrieveMetadataForTable(self, table):
        self.trinoCursor.execute("SHOW COLUMNS FROM " + table)
        rows = self.trinoCursor.fetchall()
        metadata = pd.DataFrame(rows)
        print(metadata[0])
        
    def Main(self):
        self.ConnectToTrino()
        self.RetrieveMetadataForTable("mariadb.drexel_people.basic_employee_info")

if __name__=="__main__":
    generateSQL = RetrieveMetadata()
    generateSQL.Main()