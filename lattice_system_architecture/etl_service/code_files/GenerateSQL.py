import trino
import pandas as pd
from Serialization import *
from TrinoConnection import *

class GenerateSQL:
    trinoCursor = None
    
    def __init__(self):
        pass

    def FormatDictionary(self, entireDict, tagToFormat):
        formattedTagDict = entireDict[tagToFormat]

        #set up "all_columns"
        formattedTagDict["all_columns"] = formattedTagDict["columns_tagged"]
        del formattedTagDict["columns_tagged"]

        #set up "all_concat_columns"
        #TODO: Set this part up
        formattedTagDict["all_concat_columns"] = []

        #set up "join_columns"
        if tagToFormat + ".join" in entireDict: #if a join tag exists for the current tag
            if len(entireDict[tagToFormat + ".join"]["columns_tagged"]) > 0: #if the join tag has been applied to columns
                formattedTagDict["join_columns"] = entireDict[tagToFormat + ".join"]["columns_tagged"]
                for joinColumn in formattedTagDict["join_columns"]: #make sure that a join column is in the "all_columns" list
                    if not joinColumn in formattedTagDict["all_columns"]:
                        allColumns = formattedTagDict["all_columns"]
                        allColumns.append(joinColumn)
                        formattedTagDict["all_columns"] = allColumns
            else:
                formattedTagDict["join_columns"] = []
        else:
            formattedTagDict["join_columns"] = []

        #set up "all_tables"
        formattedTagDict["all_tables"] = []
        taggedTables = []
        for column in formattedTagDict["all_columns"]:
            table = column[:-(column[::-1].index(".")+1)]
            if not table in taggedTables: #each table added should be unique
                allTables = formattedTagDict["all_tables"]
                allTables.append(table)
                formattedTagDict["all_tables"] = allTables
                taggedTables.append(table)

        return(formattedTagDict)

    #Trino has a query sent to it and the results are stored in a Pandas dataframe
    def ExecuteTrinoQuery(self, query):
        self.trinoCursor.execute(query)
        rows = self.trinoCursor.fetchall()
        columns = [column[0] for column in self.trinoCursor.description]
        queryResult = pd.DataFrame(rows, columns=columns)
        print(queryResult) #results are currently printed but will be written to CSVs later

    #the different portions of a SQL query are configured and added together as a string
    def ConvertColumnsToSQL(self, tagDict):        
        generatedSQLStatement = ""
        sqlColumns = "SELECT "
        sqlFrom = ""
        sqlInnerJoin = ""

        #columns to SELECT are constructed
        for column in tagDict["all_columns"]:
            sqlColumns = sqlColumns + column + ", "

        #add concatenated columns to the SELECT if requested
        if len(tagDict["all_concat_columns"]) > 0:
            for allConcatColumns in tagDict["all_concat_columns"]:
                sqlColumns = sqlColumns + "concat("
                for concatColumns in allConcatColumns["concat_columns"]:
                    sqlColumns = sqlColumns + concatColumns["concat_column"] + ", \' \', "
                sqlColumns = sqlColumns[:-7] #removes remaining space and commas
                sqlColumns = sqlColumns + ") AS " + allConcatColumns["concat_name"] + ", "

        sqlColumns = sqlColumns[:-2] #removes remaining comma

        #FROM text is configured
        sqlFrom = sqlFrom + "\nFROM " + tagDict["all_tables"][0]

        isFirstIteration = True #utilized to skip the first iteration
        if len(tagDict["all_tables"]) > 1:
            taggedColumnsTables = tagDict["all_tables"]
            for table in taggedColumnsTables:
                if isFirstIteration:
                    isFirstIteration = False
                    continue
                sqlInnerJoin = sqlInnerJoin + "\nINNER JOIN " #inner joins are constructed for as many joins are set to take place
                sqlOn = "ON "
                for joinColumn in tagDict["join_columns"]:
                    if joinColumn[:-(joinColumn[::-1].index(".")+1)] == table:
                        sqlOn = sqlOn + joinColumn + " = "
                        break
                for joinColumn in tagDict["join_columns"]:
                    if joinColumn[:-(joinColumn[::-1].index(".")+1)] == taggedColumnsTables[0]: #retrives the FROM table's join column
                        sqlOn = sqlOn + joinColumn
                        break
                sqlInnerJoin = sqlInnerJoin + table + " " + sqlOn

            generatedSQLStatement = generatedSQLStatement + sqlColumns + sqlFrom + sqlInnerJoin #the final SQL statement is constructed
        else:
            generatedSQLStatement = generatedSQLStatement + sqlColumns + sqlFrom #the final SQL statement is constructed

        return generatedSQLStatement
        
    def Main(self):
        self.trinoCursor = TrinoConnection.getActiveTrinoCursor()

        tagsDict = Serialization.Deserialize("../serialized_data/SerializedTags.txt") #TODO: Change off temp dir
        for tag in tagsDict:
            if (len(tagsDict[tag]["columns_tagged"]) > 0) and (not ".join" in tag) and (not ".concat" in tag):
                formattedTagDict = self.FormatDictionary(tagsDict, tag)
                self.ExecuteTrinoQuery(self.ConvertColumnsToSQL(formattedTagDict))
                #TODO: Consider error handling for if tags aren't applied properly (such as .joins missing) (Maybe just ignore a table if it doesn't have a .join when there are at least 2 tables)
                #TODO: Write to CSV

if __name__ == "__main__":
    generateSQL = GenerateSQL()
    generateSQL.Main()