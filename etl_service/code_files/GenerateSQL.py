import trino
import pandas as pd

class GenerateSQL:
    trinoCursor = None

    #example of tagged columns after being deserialized and parsed
    taggedColumnsList = [
                            {"tag_name": "Housing",
                            "all_columns": 
                            [
                                "cassandra.finances.housing_costs.residence_name", 
                                "cassandra.finances.housing_costs.room_style", 
                                "cassandra.finances.housing_costs.maximum_monthly_cost", 
                                "cassandra.finances.housing_costs.minimum_monthly_cost",
                                "postgres.campus_life.housing_options.residence_name",
                                "postgres.campus_life.housing_options.address",
                                "postgres.campus_life.housing_options.is_affiliated_housing"
                            ],
                            "join_columns":
                            [
                                "cassandra.finances.housing_costs.residence_name",
                                "postgres.campus_life.housing_options.residence_name"
                            ],
                            "all_tables":
                            [
                                "cassandra.finances.housing_costs",
                                "postgres.campus_life.housing_options"
                            ]
                            }
                        ]
    
    def __init__(self):
        pass

    def ConnectToTrino(self):
        trinoConnection = trino.dbapi.connect(
            host="localhost",
            port=8080,
            user="trino"
        )
        self.trinoCursor = trinoConnection.cursor() #what is being used to send queries to Trino

    #Trino has a query sent to it and the results are stored in a Pandas dataframe
    def ExecuteTrinoQuery(self, query):
        self.trinoCursor.execute(query)
        rows = self.trinoCursor.fetchall()
        columns = [column[0] for column in self.trinoCursor.description]
        queryResult = pd.DataFrame(rows, columns=columns)
        print(queryResult) #results are currently printed but will be written to CSVs later

    #the different portions of a SQL query are configured and added together as a string
    def ConvertColumnsToSQL(self, tag):
        taggedColumnsDict = {}
        
        generatedSQLStatement = ""
        sqlColumns = "SELECT "
        sqlFrom = ""
        sqlInnerJoin = ""

        #specified tag is found in the dictionary
        for taggedColumnsListElement in self.taggedColumnsList:
            if taggedColumnsListElement["tag_name"] == tag:
                taggedColumnsDict = taggedColumnsListElement
                break

        #columns to SELECT are constructed
        for column in taggedColumnsDict["all_columns"]:
            sqlColumns = sqlColumns + column + ", "
        sqlColumns = sqlColumns[:-2]
        
        #FROM text is configured
        sqlFrom = sqlFrom + "\nFROM " + taggedColumnsDict["all_tables"][0]

        isFirstIteration = True #utilized to skip the first iteration
        if len(taggedColumnsDict["all_tables"]) > 1:
            taggedColumnsTables = taggedColumnsDict["all_tables"]
            for table in taggedColumnsTables:
                if isFirstIteration:
                    isFirstIteration = False
                    continue
                sqlInnerJoin = sqlInnerJoin + "\nINNER JOIN " #inner joins are constructed for as many joins are set to take place
                sqlOn = "ON "
                for joinColumn in taggedColumnsDict["join_columns"]:
                    if joinColumn[:-(joinColumn[::-1].index(".")+1)] == table:
                        sqlOn = sqlOn + joinColumn + " = "
                        break
                for joinColumn in taggedColumnsDict["join_columns"]:
                    if joinColumn[:-(joinColumn[::-1].index(".")+1)] == taggedColumnsTables[0]: #retrives the FROM table's join column
                        sqlOn = sqlOn + joinColumn
                        break
                sqlInnerJoin = sqlInnerJoin + table + " " + sqlOn

            generatedSQLStatement = generatedSQLStatement + sqlColumns + sqlFrom + sqlInnerJoin #the final SQL statement is constructed
        else:
            generatedSQLStatement = generatedSQLStatement + sqlColumns + sqlFrom #the final SQL statement is constructed

        return generatedSQLStatement
        
    def Main(self):
        self.ConnectToTrino()
        self.ExecuteTrinoQuery(self.ConvertColumnsToSQL("Housing"))

if __name__=="__main__":
    generateSQL = GenerateSQL()

    generateSQL.Main()