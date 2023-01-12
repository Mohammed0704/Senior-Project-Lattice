import trino
import pandas as pd
import os.path

currentDirectory = os.getcwd()

class GenerateSQL:
    trinoCursor = None

    def __init__(self):
        pass

    def ConnectToTrino(self):
        trinoConnection = trino.dbapi.connect(
            host="localhost",
            port=8080,
            user="trino",
        )

        self.trinoCursor = trinoConnection.cursor() #what is being used to send queries to Trino  

    #Trino has a query sent to it and the results are stored in a Pandas dataframe
    def ExecuteTrinoQuery(self, query):
        self.trinoCursor.execute(query)
        rows = self.trinoCursor.fetchall()
        columns = [column[0] for column in self.trinoCursor.description]
        queryResult = pd.DataFrame(rows, columns=columns)
        print(queryResult)
        queryResult.to_csv(currentDirectory + '/etl_service/TrinoQueryToCSVOutput/TrinoQuery{}.csv'.format(pd.datetime.now().strftime("%Y-%m-%d %H%M%S")))

        
    def Main(self):
        UserQuery = input('Enter in TrinoDB Query to Output to a CSV file:')
        self.ConnectToTrino()
        self.ExecuteTrinoQuery(UserQuery)


if __name__=="__main__":
    generateSQL = GenerateSQL()

    generateSQL.Main()
