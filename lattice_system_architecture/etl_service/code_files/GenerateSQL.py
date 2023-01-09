import trino
import pandas as pd

class GenerateSQL:
    trinoCursor = None
    trinoHost = "localhost"
    trinoPort = 8080
    trinoUser = "user"

    #example of tagged columns after being deserialized and parsed
    taggedColumnsList = [
                            {
                            "tag_name": "Housing",
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
                            "all_concat_columns":
                            [
                                {
                                    "concat_name": "test", "concat_columns": 
                                [
                                    {
                                        "concat_column": "cassandra.finances.housing_costs.room_style",
                                        "concat_column_order": 1
                                    },
                                    {
                                        "concat_column": "cassandra.finances.housing_costs.maximum_monthly_cost",
                                        "concat_column_order": 2
                                    }
                                ]
                                },
                                {
                                    "concat_name": "another_test", "concat_columns": 
                                [
                                    {
                                        "concat_column": "postgres.campus_life.housing_options.address",
                                        "concat_column_order": 1
                                    },
                                    {
                                        "concat_column": "postgres.campus_life.housing_options.residence_name",
                                        "concat_column_order": 2
                                    }
                                ]
                                }
                            ],
                            "join_columns":
                            [
                                "cassandra.finances.housing_costs.residence_name",
                                "postgres.campus_life.housing_options.residence_name"
                            ],
                            "join_concat_columns":
                            [
                            ],
                            "all_tables":
                            [
                                "cassandra.finances.housing_costs",
                                "postgres.campus_life.housing_options"
                            ]
                            }
                        ]
    
    #second example of tagged columns after being deserialized and parsed
    taggedColumnsList2 = [
                            {
                            "tag_name": "Employee",
                            "all_columns": 
                            [
                                "mariadb.drexel_people.basic_employee_info.first_name", 
                                "mariadb.drexel_people.basic_employee_info.last_name", 
                                "mariadb.drexel_people.basic_employee_info.email", 
                                "cassandra.finances.employee_salaries.full_name",
                                "cassandra.finances.employee_salaries.job_title"
                            ],
                            "all_concat_columns":
                            [
                            ],
                            "join_columns":
                            [
                                "cassandra.finances.employee_salaries.full_name"
                            ],
                            "join_concat_columns":
                            [
                                {
                                    "concat_name": "f_name", "concat_columns": 
                                [
                                    {
                                        "concat_column": "mariadb.drexel_people.basic_employee_info.first_name",
                                        "concat_column_order": 1
                                    },
                                    {
                                        "concat_column": "mariadb.drexel_people.basic_employee_info.last_name",
                                        "concat_column_order": 2
                                    }
                                ]
                                }
                            ],
                            "all_tables":
                            [
                                "mariadb.drexel_people.basic_employee_info",
                                "cassandra.finances.employee_salaries"
                            ]
                            }
                        ]

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
        for taggedColumnsListElement in self.taggedColumnsList2:
            if taggedColumnsListElement["tag_name"] == tag:
                taggedColumnsDict = taggedColumnsListElement
                break

        #columns to SELECT are constructed
        for column in taggedColumnsDict["all_columns"]:
            sqlColumns = sqlColumns + column + ", "

        #add concatenated columns to the SELECT if requested
        if len(taggedColumnsDict["all_concat_columns"]) > 0:
            for allConcatColumns in taggedColumnsDict["all_concat_columns"]:
                sqlColumns = sqlColumns + "concat("
                for concatColumns in allConcatColumns["concat_columns"]:
                    sqlColumns = sqlColumns + concatColumns["concat_column"] + ", \' \', "
                sqlColumns = sqlColumns[:-7] #removes remaining space and commas
                sqlColumns = sqlColumns + ") AS " + allConcatColumns["concat_name"] + ", "

        sqlColumns = sqlColumns[:-2] #removes remaining comma


        
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
                    if joinColumn[:-(joinColumn[::-1].index(".")+1)] == table: #parses the column name out and compares to the current table
                        sqlOn = sqlOn + joinColumn + " = "
                        break
                
                fromTableJoinColumn = ""
                for joinColumn in taggedColumnsDict["join_columns"]:
                    if joinColumn[:-(joinColumn[::-1].index(".")+1)] == taggedColumnsTables[0]: #retrives the FROM table's join column
                        sqlOn = sqlOn + joinColumn
                        fromTableJoinColumn = joinColumn
                        break

                for joinConcatColumns in taggedColumnsDict["join_concat_columns"]:
                    sqlOn = sqlOn + "concat("
                    for concatColumns in joinConcatColumns["concat_columns"]:
                        concatColumn = concatColumns["concat_column"]
                        print("----")
                        print(concatColumn[:-(concatColumn[::-1].index(".")+1)])
                        print(table)
                        print("----\n----")
                        #if concatColumn[:-(concatColumn[::-1].index(".")+1)] == table:
                        for concatColumns in joinConcatColumns["concat_columns"]:
                            sqlOn = sqlOn + concatColumns["concat_column"] + ", \' \', "
                        sqlOn = sqlOn[:-7] #removes remaining space and commas
                        sqlOn = sqlOn + ") AS " + joinConcatColumns["concat_name"] + " = " + fromTableJoinColumn + ", "

                
                sqlInnerJoin = sqlInnerJoin + table + " " + sqlOn

            generatedSQLStatement = generatedSQLStatement + sqlColumns + sqlFrom + sqlInnerJoin #the final SQL statement is constructed
        else:
            generatedSQLStatement = generatedSQLStatement + sqlColumns + sqlFrom #the final SQL statement is constructed

        print("\nGenerated SQL Statement:\n" + generatedSQLStatement + "\n")
        return generatedSQLStatement
        
    def Main(self):
        self.ConnectToTrino()
        #self.ExecuteTrinoQuery(self.ConvertColumnsToSQL("Housing"))
        self.ExecuteTrinoQuery(self.ConvertColumnsToSQL("Employee"))

if __name__=="__main__":
    generateSQL = GenerateSQL()

    generateSQL.Main()