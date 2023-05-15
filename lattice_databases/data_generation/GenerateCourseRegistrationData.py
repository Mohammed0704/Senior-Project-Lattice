import json
import csv
import sys

filePathCourse = "./../mongodb/data_files/MongoDB-course-restrictions.json"
filePathOutput = "./../postgres/data_files/Postgres-course_requirements.csv"

with open(filePathCourse, 'r') as jsonClass:
    courseData = json.load(jsonClass)

    outputHeaders = ["cr_id", "rel_id", "req_choices"]
    outputList = []

    for course in courseData:
        courseCode = course["Course Code"]
        courseContentList = []
        firstLevelNum = 1
        secondLevelNum = 1
        relationshipID = courseCode
        requirementChoices = ""

        prerequisites = course["Prerequisites"]

        if prerequisites != "":
            prerequisites = prerequisites.replace(" or ", ", ")
            prerequisites = prerequisites.replace(" and ", "; ")

            #NOTE: Concurrently text is messed up, so this "fixes it"
            concurrentlyText = " (Can be taken Concurrently)"
            findValue = prerequisites.find(concurrentlyText)
            if findValue != -1:
                if findValue + len(concurrentlyText) == len(prerequisites):
                    prerequisites = prerequisites.replace(concurrentlyText, "").strip()
                else:
                    prerequisites = prerequisites.replace(concurrentlyText, "; ")

            if "(" not in prerequisites and ")" not in prerequisites:
                outputList.append([courseCode + "-" + str(firstLevelNum), relationshipID, prerequisites])
            else:
                #retrieves all the parenthesis text
                withinList = []
                while "(" in prerequisites or ")" in prerequisites:
                    withinText = prerequisites[prerequisites.find("("):prerequisites.find(")")+1]
                    withinList.append(withinText)
                    prerequisites = prerequisites.replace(withinText, "")

                #if everything is in parenthesis
                if prerequisites == "":
                    outputList.append([courseCode + "-" + str(firstLevelNum), relationshipID, withinList[0].replace("(", "").replace(")", "")])
                    continue

                courseRequirementsList = []
                for withinListElement in withinList:
                    courseRequirementID =  courseCode + "-" + str(firstLevelNum) + "-" + str(secondLevelNum)
                    courseRequirementsList.append([courseRequirementID, courseCode + "-" + str(firstLevelNum), withinListElement.replace("(", "").replace(")", "")]) #does not currently know what ID to map to
                    secondLevelNum += 1
                    #NOTE: TEMP CHANGE MAYBE
                
                for courseRequirementsIndex in range(len(courseRequirementsList)):
                    tempPrerequisites = prerequisites.replace(",", ";")

                    #Finds the nth occurence
                    symbolValue = -1
                    for i in range(0, courseRequirementsIndex + 1):
                        symbolValue = tempPrerequisites.find(";", symbolValue + 1)

                    courseRequirement = courseRequirementsList[courseRequirementsIndex][0]
                    if symbolValue == 0:
                        prerequisites = courseRequirement + prerequisites[symbolValue:len(prerequisites)]
                    else:
                        if symbolValue == -1 and len(courseRequirementsList) != courseRequirementsIndex:
                            prerequisites = prerequisites + " " + courseRequirement + prerequisites[symbolValue:len(prerequisites)]
                        else:
                            prerequisites = prerequisites[:symbolValue + 1] + " " + courseRequirement + prerequisites[symbolValue:len(prerequisites)]
                
                #NOTE:messy cleanup; it would be more ideal to dissect the individual issues in the code
                prerequisites = prerequisites.strip()
                if prerequisites.endswith(",") or prerequisites.endswith(";"):
                    prerequisites = prerequisites[:-1]
                prerequisites = prerequisites.replace(" ;", "")
                prerequisites = prerequisites.replace(" ,", "")
                prerequisites = prerequisites.replace("  ", " ")
                    
                prerequisitesSplit = None
                if "; " in prerequisites:
                    prerequisitesSplit = prerequisites.split("; ")
                elif ", " in prerequisites:
                    prerequisitesSplit = prerequisites.split(", ")

                #NOTE: These oddly formatted ones are currently just being excluded
                if ";" in prerequisites and "," in prerequisites:
                    continue

                outputList.append([courseCode + "-" + str(firstLevelNum), courseCode, prerequisites])

                for courseRequirement in courseRequirementsList:
                    outputList.append(courseRequirement)

    with open(filePathOutput, 'w', newline='') as csvOutput:
        writer = csv.writer(csvOutput)

        writer.writerow(outputHeaders)
        writer.writerows(outputList)