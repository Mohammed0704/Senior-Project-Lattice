import os
import json
import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

'''
    (Structure)
    Database System:
        Database:
            Table:
                Fields
    
    REF: https://termmasterschedule.drexel.edu/webtms_du/
    MongoDB:
        classes:
            crn
            description
            associated_term
            instruction_type
            instruction_method
            instructor
            grade_mode
            associated_course_code
            section
            meeting_days
            campus
        
'''

def driverSetup():
    # This can be used to add additional options like a download path if you wanted your web scrapper to hit a button and download a file on a website 
    options = Options()
    # options.headless = True # If false, the browser window will pop up
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    return driver

def main():
    
    classesInfo = []
    classesInstructionInfo = []
    driver = driverSetup()
    
    driver.get("https://termmasterschedule.drexel.edu/webtms_du/")
    
    # Gather all links to dedicated term master
    linkSections = driver.find_elements(By.XPATH, "/html/body/table/tbody/tr[2]/td/table[2]/tbody/tr[2]/td[3]/table/tbody/tr[3]/td/table")
    for block in linkSections:
        links = [link.get_attribute("href") for link in block.find_elements(By.XPATH, ".//a")]

        classLinks2022 = links[0:4]
        classLinks2021 = links[4:8]

    
    for link in classLinks2022:
        driver.get(link)
        collegeSection = driver.find_elements(By.XPATH, "//*[@id=\"sideLeft\"]")

        for block in collegeSection:
            collegeLinks = [path.get_attribute("href") for path in block.find_elements(By.XPATH, ".//a")]
        
        for collegeLink in collegeLinks:
            driver.get(collegeLink)
            
            subjectSection = driver.find_elements(By.XPATH, "/html/body/table/tbody/tr[2]/td/table[2]/tbody/tr[3]/td[2]/table/tbody/tr[2]/td/table/tbody/tr[2]/td")
            for block in subjectSection:
                subjectLinks = [path.get_attribute("href") for path in block.find_elements(By.XPATH, ".//div/a")]

            for subjectLink in subjectLinks:
                driver.get(subjectLink)
    
                scheduleHeader = driver.find_element(By.XPATH, "/html/body/table/tbody/tr[2]/td/table[2]/tbody/tr[2]/td/div").text
                quarterNumber = int(scheduleHeader.split()[-1].replace("(", "").replace(")", "")[-2:])
                if quarterNumber == 15:
                    associated_term = "Fall Quarter 22-23"
                elif quarterNumber == 25:
                    associated_term = "Winter Quarter 22-23"
                elif quarterNumber == 35:
                    associated_term = "Spring Quarter 22-23"
                elif quarterNumber == 45:
                    associated_term = "Summer Quarter 22-23"

                classInfoDict = {}
                classInfoInstructionDict = {}
                classSectionRows = driver.find_elements(By.XPATH, "//*[@id=\"sortableTable\"]/tbody[1]/tr")
                for row in classSectionRows:
                    meetingDays = ""
                    meetingDaysObreviation = row.find_elements(By.TAG_NAME, "td")[7].text.split("\n")[0].split()[0].strip()
                    if meetingDaysObreviation.lower() == "tbd":
                        meetingDays = "TBD"
                    else:
                        i = 0
                        for letter in meetingDaysObreviation.lower():
                            if letter == "m":
                                meetingDays += "Monday"
                            elif letter == "t":
                                meetingDays += "Tuesday"
                            elif letter == "w":
                                meetingDays += "Wednesday"
                            elif letter == "r":
                                meetingDays += "Thursday"
                            elif letter == "f":
                                meetingDays += "Friday"
                            if len(meetingDaysObreviation.lower()) - 1 != i:
                                meetingDays += ", "
                            i += 1
                    classInfoDict = {
                        "associated_course_code" : row.find_elements(By.TAG_NAME, "td")[0].text + " " + row.find_elements(By.TAG_NAME, "td")[1].text,
                        "instruction_type" : row.find_elements(By.TAG_NAME, "td")[2].text,
                        "instruction_methond" : row.find_elements(By.TAG_NAME, "td")[3].text,
                        "section" : row.find_elements(By.TAG_NAME, "td")[4].text,
                        "crn" : row.find_elements(By.TAG_NAME, "td")[5].text,
                        "description" : row.find_elements(By.TAG_NAME, "td")[6].text,
                        "meeting_days" : meetingDays, 
                        "instructor" : row.find_elements(By.TAG_NAME, "td")[-1].text, 
                        "associated_term" : associated_term
                    }
                    classInfoInstructionDict = {
                        "crn" : row.find_elements(By.TAG_NAME, "td")[5].text,
                        "professor" : row.find_elements(By.TAG_NAME, "td")[-1].text,
                        "instruction_type" : row.find_elements(By.TAG_NAME, "td")[2].text,
                        "instruction_methond" : row.find_elements(By.TAG_NAME, "td")[3].text
                    }
                    classesInfo.append(classInfoDict)
                    classesInstructionInfo.append(classInfoInstructionDict)


    for link in classLinks2021:
        driver.get(link)
        collegeSection = driver.find_elements(By.XPATH, "//*[@id=\"sideLeft\"]")

        for block in collegeSection:
            collegeLinks = [path.get_attribute("href") for path in block.find_elements(By.XPATH, ".//a")]
        
        for collegeLink in collegeLinks:
            driver.get(collegeLink)
            
            subjectSection = driver.find_elements(By.XPATH, "/html/body/table/tbody/tr[2]/td/table[2]/tbody/tr[3]/td[2]/table/tbody/tr[2]/td/table/tbody/tr[2]/td")
            for block in subjectSection:
                subjectLinks = [path.get_attribute("href") for path in block.find_elements(By.XPATH, ".//div/a")]

            for subjectLink in subjectLinks:
                driver.get(subjectLink)
    
                scheduleHeader = driver.find_element(By.XPATH, "/html/body/table/tbody/tr[2]/td/table[2]/tbody/tr[2]/td/div").text
                quarterNumber = int(scheduleHeader.split()[-1].replace("(", "").replace(")", "")[-2:])
                if quarterNumber == 15:
                    associated_term = "Fall Quarter 21-22"
                elif quarterNumber == 25:
                    associated_term = "Winter Quarter 21-22"
                elif quarterNumber == 35:
                    associated_term = "Spring Quarter 21-22"
                elif quarterNumber == 45:
                    associated_term = "Summer Quarter 21-22"

                classInfoDict = {}
                classInfoInstructionDict = {}
                classSectionRows = driver.find_elements(By.XPATH, "//*[@id=\"sortableTable\"]/tbody[1]/tr")
                for row in classSectionRows:
                    meetingDays = ""
                    meetingDaysObreviation = row.find_elements(By.TAG_NAME, "td")[7].text.split("\n")[0].split()[0].strip()
                    if meetingDaysObreviation.lower() == "tbd":
                        meetingDays = "TBD"
                    else:
                        i = 0
                        for letter in meetingDaysObreviation.lower():
                            if letter == "m":
                                meetingDays += "Monday"
                            elif letter == "t":
                                meetingDays += "Tuesday"
                            elif letter == "w":
                                meetingDays += "Wednesday"
                            elif letter == "r":
                                meetingDays += "Thursday"
                            elif letter == "f":
                                meetingDays += "Friday"
                            if len(meetingDaysObreviation.lower()) - 1 != i:
                                meetingDays += ", "
                            i += 1
                    classInfoDict = {
                        "associated_course_code" : row.find_elements(By.TAG_NAME, "td")[0].text + " " + row.find_elements(By.TAG_NAME, "td")[1].text,
                        "instruction_type" : row.find_elements(By.TAG_NAME, "td")[2].text,
                        "instruction_methond" : row.find_elements(By.TAG_NAME, "td")[3].text,
                        "section" : row.find_elements(By.TAG_NAME, "td")[4].text,
                        "crn" : row.find_elements(By.TAG_NAME, "td")[5].text,
                        "description" : row.find_elements(By.TAG_NAME, "td")[6].text,
                        "meeting_days" : meetingDays, 
                        "instructor" : row.find_elements(By.TAG_NAME, "td")[-1].text, 
                        "associated_term" : associated_term
                    }
                    classInfoInstructionDict = {
                        "crn" : row.find_elements(By.TAG_NAME, "td")[5].text,
                        "professor" : row.find_elements(By.TAG_NAME, "td")[-1].text,
                        "instruction_type" : row.find_elements(By.TAG_NAME, "td")[2].text,
                        "instruction_methond" : row.find_elements(By.TAG_NAME, "td")[3].text
                    }
                    classesInfo.append(classInfoDict)
                    classesInstructionInfo.append(classInfoInstructionDict)
    
    cwd = os.getcwd()
    
    courseInfoPath = cwd + os.sep + "MongoDB_Data" + os.sep + "MongoDB-class-info.json"
    courseRestrictionsPath = cwd + os.sep + "MongoDB_Data" + os.sep + "MongoDB-class-instruction-info.json"

    with open(courseInfoPath, "w") as jsonFile:
        json.dump(classesInfo, jsonFile, indent=4)
    with open(courseRestrictionsPath, "w") as jsonFile:
        json.dump(classesInstructionInfo, jsonFile, indent=4)
        
        
if __name__ == "__main__":
    main()