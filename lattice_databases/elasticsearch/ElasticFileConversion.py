import csv 
import json 

def ConvertCSVToESJSON(indexName, csvFilePath, jsonFilePath):
    with open(csvFilePath, encoding='utf-8') as csvf: 
        with open(jsonFilePath, 'w', encoding='utf-8') as jsonf:
            csvReader = csv.DictReader(csvf) 
            currentIndex = 1
            for row in csvReader: 
                jsonf.write("{ \"index\":{\"_index\": \"" + indexName + "\", \"_id\": \"" + str(currentIndex) + "\" }}")
                jsonf.write("\n")
                for col in row:
                    if row[col].lower() == "false":
                        row[col] = False
                    elif row[col].lower() == "true":
                        row[col] = True
                    elif isinstance(row[col], str):
                        row[col] = row[col].strip()
                rowJSON = json.dumps(row)
                jsonf.write(rowJSON)
                jsonf.write("\n")
                currentIndex += 1

def ConvertTextLogToESJSON(indexName, actionedObject, logFilePath, jsonFilePath):
    logFileLogs = open(logFilePath, "r")
    logs = logFileLogs.readlines()

    with open(jsonFilePath, 'w', encoding='utf-8') as jsonf:
        currentIndex = 1
        for line in logs:
            if line.startswith("----"):
                continue
            else:
                jsonf.write("{ \"index\":{\"_index\": \"" + indexName + "\", \"_id\": \"" + str(currentIndex) + "\" }}")
                jsonf.write("\n")
                currentIndex += 1
            
            log = line.split(" | ")
            date_time = log[0].strip(r"[|]").split(" ")
            date = date_time[0]
            time = date_time[1]

            doc = {
                "drexelID": log[2][log[2].index(":")+2:],
                "name": log[1],
                "action": log[3],
                actionedObject: log[4].strip(),
                "date": date,
                "time": time
            }

            rowJSON = json.dumps(doc)
            jsonf.write(rowJSON)
            jsonf.write("\n")
          
csvFilePath = r'./elasticsearch/data_files/Elasticsearch-additional_area_of_study.csv'
jsonFilePath = r'./elasticsearch/data_files/Elasticsearch-additional_area_of_study.json'
ConvertCSVToESJSON("area_of_study", csvFilePath, jsonFilePath)

csvFilePath = r'./elasticsearch/data_files/Elasticsearch-drexel_additional_education_info-departments.csv'
jsonFilePath = r'./elasticsearch/data_files/Elasticsearch-drexel_additional_education_info-departments.json'
ConvertCSVToESJSON("departments", csvFilePath, jsonFilePath)

csvFilePath = r'./elasticsearch/data_files/Elasticsearch-programs.csv'
jsonFilePath = r'./elasticsearch/data_files/Elasticsearch-programs.json'
ConvertCSVToESJSON("programs", csvFilePath, jsonFilePath)

logTextFilePath = r'./elasticsearch/data_files/logs/LibraryLogs.txt'
jsonFilePath = r'./elasticsearch/data_files/logs/LibraryLogs.json'
ConvertTextLogToESJSON("hagerty_library_log", "location", logTextFilePath, jsonFilePath)

logTextFilePath = r'./elasticsearch/data_files/logs/RecreationCenterLogs.txt'
jsonFilePath = r'./elasticsearch/data_files/logs/RecreationCenterLogs.json'
ConvertTextLogToESJSON("recreation_center_logs", "location", logTextFilePath, jsonFilePath)

logTextFilePath = r'./elasticsearch/data_files/logs/SystemsLogs.txt'
jsonFilePath = r'./elasticsearch/data_files/logs/SystemsLogs.json'
ConvertTextLogToESJSON("systems_logs", "system", logTextFilePath, jsonFilePath)