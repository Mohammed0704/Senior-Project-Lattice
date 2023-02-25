from code_files.Serialization import *

class SQLGeneration:
    
    def __init__(self):
        pass

    def formatDictionary(self, entireDict, tagToFormat):
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
    
    def formatColumn(self, fullColumn):
        table = fullColumn[:-(fullColumn[::-1].index(".")+1)]
        column = fullColumn[fullColumn.rfind(".") + 1 : len(fullColumn)]
        if " " in column: #if there is a space in the column name
            return table + ".\"" + column + "\""
        else:
            return fullColumn

    #the different portions of a SQL query are configured and added together as a string
    def convertColumnsToSQL(self, tagDict):        
        generatedSQLStatement = ""
        sqlColumns = "SELECT "
        sqlFrom = ""
        sqlInnerJoin = ""

        #columns to SELECT are constructed
        for column in tagDict["all_columns"]:
            sqlColumns = sqlColumns + self.formatColumn(column) + ", "

        #add concatenated columns to the SELECT if requested
        if len(tagDict["all_concat_columns"]) > 0:
            for allConcatColumns in tagDict["all_concat_columns"]:
                sqlColumns = sqlColumns + "concat("
                for concatColumns in allConcatColumns["concat_columns"]:
                    sqlColumns = sqlColumns + self.formatColumn(concatColumns["concat_column"]) + ", \' \', "
                sqlColumns = sqlColumns[:-7] #removes remaining space and commas
                sqlColumns = sqlColumns + ") AS " + self.formatColumn(allConcatColumns["concat_name"]) + ", "

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
                        sqlOn = sqlOn + self.formatColumn(joinColumn) + " = "
                        break
                for joinColumn in tagDict["join_columns"]:
                    if joinColumn[:-(joinColumn[::-1].index(".")+1)] == taggedColumnsTables[0]: #retrives the FROM table's join column
                        sqlOn = sqlOn + self.formatColumn(joinColumn)
                        break
                sqlInnerJoin = sqlInnerJoin + table + " " + sqlOn

            generatedSQLStatement = generatedSQLStatement + sqlColumns + sqlFrom + sqlInnerJoin #the final SQL statement is constructed
        else:
            generatedSQLStatement = generatedSQLStatement + sqlColumns + sqlFrom #the final SQL statement is constructed

        return generatedSQLStatement
        
    def generateQuery(self, tag, tagsDict):
        if (len(tagsDict[tag]["columns_tagged"]) > 0) and (not ".join" in tag) and (not ".concat" in tag):
            formattedTagDict = self.formatDictionary(tagsDict, tag)
            return self.convertColumnsToSQL(formattedTagDict)
            #TODO: Consider error handling for if tags aren't applied properly (such as .joins missing) (Maybe just ignore a table if it doesn't have a .join when there are at least 2 tables)
        else:
            return None