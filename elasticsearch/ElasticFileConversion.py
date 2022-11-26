import csv 
import json 
import collections
orderedDict = collections.OrderedDict()
from collections import OrderedDict

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
          
csvFilePath = r'./elasticsearch/data_files/Elasticsearch-additional_area_of_study.csv'
jsonFilePath = r'./elasticsearch/data_files/Elasticsearch-additional_area_of_study.json'
ConvertCSVToESJSON("area_of_study", csvFilePath, jsonFilePath)

csvFilePath = r'./elasticsearch/data_files/Elasticsearch-drexel_additional_education_info-departments.csv'
jsonFilePath = r'./elasticsearch/data_files/Elasticsearch-drexel_additional_education_info-departments.json'
ConvertCSVToESJSON("departments", csvFilePath, jsonFilePath)

csvFilePath = r'./elasticsearch/data_files/Elasticsearch-programs.csv'
jsonFilePath = r'./elasticsearch/data_files/Elasticsearch-programs.json'
ConvertCSVToESJSON("programs", csvFilePath, jsonFilePath)