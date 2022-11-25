import pandas as pd
from ElasticInterface import Elastic

import datetime

def createIndices(es):
    
    es.deleteIndex("gym_logs")
    es.deleteIndex("hagerty_library_logs")
    es.deleteIndex("drexel_websites_logs")
    es.deleteIndex("attendance_log")
    es.deleteIndex("departments")
    es.deleteIndex("programs")
    es.deleteIndex("areas_of_study")
    
    properties = []
    properties.append(("drexelid", { "type": "text", "fields": { "keyword": { "type": "keyword", "ignore_above": 16 } } }))
    properties.append(("name", { "type": "text" }))
    properties.append(("action", { "type": "text" }))
    properties.append(("date", { "type": "date", "format": "MM/dd/yyyy" }))
    properties.append(("time", { "type": "date", "format": "HH:mm:ss" }))
    properties.append(("location", { "type": "text" }))
    es.createIndex("gym_log", properties)
    es.createIndex("hagerty_library_log", properties)
    
    properties[len(properties)-1] = ("system", { "type": "text" })
    es.createIndex("drexel_websites_log", properties)
    
    properties[len(properties)-1] = ("class", { "type": "text" })
    properties.append(("crn", { "type": "text" }))
    es.createIndex("attendance_log", properties)
    
    properties.clear()
    properties.append(("departmentname", { "type": "text" }))
    properties.append(("url", { "type": "text" }))
    properties.append(("hasfieldsite", { "type": "boolean"}))
    es.createIndex("departments", properties)
    
    properties.clear()
    properties.append(("programname", { "type": "text" }))
    properties.append(("url", { "type": "text" }))
    properties.append(("calendartype", { "type": "text" }))
    es.createIndex("programs", properties)
    
    properties.clear()
    properties.append(("name", { "type": "text" }))
    properties.append(("description", { "type": "text" }))
    properties.append(("hasmajor", { "type": "boolean"}))
    properties.append(("hasminor", { "type": "boolean"}))
    properties.append(("hascirtificate", { "type": "boolean"}))
    es.createIndex("areas_of_study", properties)
    
    #es.post(index, "ves35", "Vincent Savarese", "signed-in", "11/20/2022", "09:30:00", "gym")
    #es.get(index, "ves35")
    #es.deleteIndex(index)

def main():
    
    es = Elastic()
    
    createIndices(es)
    
    csvtimer = datetime.datetime.today()
    areasOfStudy = pd.read_csv("Elasticsearch-additional_area_of_study.csv")
    areasOfStudyDict = areasOfStudy.to_dict(orient='records')
    for row in areasOfStudyDict:
        es.post("areas_of_study", {
            "name": row["Name"],
            "description": row["Description"],
            "hasmajor": row["Has Major"],
            "hasminor": row["Has Minor"],
            "hascirtificate": row["Has Certificate"]
        })
    
    departments = pd.read_csv("Elasticsearch-drexel_additional_education_info-departments.csv")
    departmentsDict = departments.to_dict(orient="records")
    for row in departmentsDict:
        es.post("departments", {
            "departmentname": row["Department Name"],
            "url": row["URL"],
            "hasfieldsite": row["Has Field Sites"]
        })
    
    programs = pd.read_csv("Elasticsearch-programs.csv")
    programsDict = programs.to_dict(orient="records")
    for row in programsDict:
        es.post("programs", {
            "programname": row["program_name"],
            "url": row["url"],
            "calendartype": row["calendar_type"]
        })
    print("CSV timer took:",(datetime.datetime.today() - csvtimer))
    
    then = datetime.datetime.today()
    libraryLogs = open("LibraryLogs.txt", "r")
    logs = libraryLogs.readlines()
    for line in logs:
        if line.startswith("----"):
            continue
        
        log = line.split(" | ")
        date_time = log[0].strip(r"[|]").split(" ")
        date = date_time[0]
        time = date_time[1]
        
        es.post("hagerty_library_logs", {
            "drexelid": log[2][log[2].index(":")+2:],
            "name": log[1],
            "action": log[3],
            "date": date,
            "time": time,
            "location": log[4]
        })
    now = datetime.datetime.today() - then
    print(now)
    exit()

if __name__ == "__main__":   
    main()