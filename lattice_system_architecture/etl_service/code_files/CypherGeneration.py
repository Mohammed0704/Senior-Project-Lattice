class CypherGeneration():
    def generateCypherCreate(self, dataObjectFileName):
        tag = dataObjectFileName[0 : dataObjectFileName.rfind(".")] #removes extension to retrieve the tag
        createQuery = ("CALL apoc.periodic.iterate(\'"
        "\nCALL apoc.load.csv(\"import/" + dataObjectFileName + "\", {header:true}) yield map as row return row"
        "\n\',\'"
        "\nCREATE (n:" + tag + ") SET n = row"
        "\n\', {batchSize:1000, iterateList:true, parallel:true})")

        if ("Neo.ClientError.Procedure.ProcedureCallFailed" not in createQuery):
            print("\nCypher query created for " + tag + "!")
        else:
            print("\nCypher query ERROR for " + tag + "!\nERROR: " + createQuery)

        return createQuery