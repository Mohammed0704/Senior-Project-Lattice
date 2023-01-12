import trino
import pandas as pd
import os.path
import datetime

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
        dataObjectTag = "Test"
        queryResult.to_csv(currentDirectory + "/etl_service/" + dataObjectTag + "_{}.csv".format(datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S"))) #writes the query to a CSV file

        
    def Main(self):
        query = "select * from mariadb.drexel_people.basic_employee_info"
        self.ConnectToTrino()
        self.ExecuteTrinoQuery(query)


if __name__=="__main__":
    generateSQL = GenerateSQL()

    generateSQL.Main()
