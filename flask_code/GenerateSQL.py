import trino
import pandas as pd

class GenerateSQL:
    trinoCursor = None


    taggedColumnsList = [
                            {"tag_name": "Housing",
                            "all_columns": 
                            [
                                "cassandra.finances.housing_costs.residence_name", 
                                "cassandra.finances.housing_costs.room_style", 
                                "cassandra.finances.housing_costs.maximum_monthly_cost", 
                                "cassandra.finances.housing_costs.minimum_monthly_cost"
                            ],
                            "join_columns":
                            [
                                "cassandra.finances.housing_costs.residence_name"
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
        self.trinoCursor = trinoConnection.cursor()

    def ExecuteTrinoQuery(self, query):
        self.trinoCursor.execute(query)
        rows = self.trinoCursor.fetchall()
        columns = [column[0] for column in self.trinoCursor.description]
        queryResult = pd.DataFrame(rows, columns=columns)
        print(queryResult)

    def Main(self):
        print(self.taggedColumnsList[0]["join_columns"])
        #self.ConnectToTrino()
        #self.ExecuteTrinoQuery("SELECT * FROM postgres.campus_life.housing_options limit 3")
        #self.ExecuteTrinoQuery("SELECT * FROM cassandra.finances.housing_costs limit 3")

if __name__=="__main__":
    generateSQL = GenerateSQL()

    generateSQL.Main()