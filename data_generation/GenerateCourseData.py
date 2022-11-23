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
    
    REF: https://catalog.drexel.edu/coursedescriptions/quarter/undergrad/
    MongoDB:
        courses:
            course_info:
                Course Code
                Course Title
                College
                Credits
            course_requirements:
                Course Code
                Pre-Requisites
                Co-Requisites
                Repeat Status
                Restrictions
        
'''

def driverSetup():
    # This can be used to add additional options like a download path if you wanted your web scrapper to hit a button and download a file on a website 
    options = Options()
    options.headless = True # If false, the browser window will pop up
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    return driver

def main():
    
    courseLinks = []
    driver = driverSetup()
    
    # database variables
    course_code = ""
    
    course_title = ""
    college = ""
    credits = ""
    
    pre_requisites = ""
    co_requisites = ""
    repeat_status = ""
    restrictions = ""
    
    driver.get("https://catalog.drexel.edu/coursedescriptions/quarter/undergrad/")
    time.sleep(5)
    
    # Gather all links to dedicated course catalogs
    linkSections = driver.find_elements(By.XPATH, "//*[@id='listCol2']/div")
    for block in linkSections:
        links = [link.get_attribute("href") for link in block.find_elements(By.XPATH, ".//a")]
        print("Num of links:", len(links))
        courseLinks.extend(links)
    
    # For each link, navigate to the page and scrape all respective information into course_info and course_restrictions collections   
    numCourses = 0
    courseInfoList = []
    courseRestrictionsList = []
    for link in courseLinks:
        
        driver.get(link)
        try:
            WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "courses")))    
            courses = driver.find_elements(By.CLASS_NAME, "courseblock")
            numCourses += len(courses)
            print(f"\nLink: {link}\nNumber of courses {len(courses)}")
            
            for course in courses:
                course_code = ""
                course_title = ""
                college = ""
                credits = ""
                pre_requisites = ""
                co_requisites = ""
                repeat_status = ""
                restrictions = ""
                
                text = course.text.split("\n")
                for line in range(len(text)):
                    if line == 0:
                        title = text[line].split(" ")
                        course_code = " ".join(title[0:2])
                        course_title = " ".join(title[2:len(title)-2])
                        credits = title[len(title)-2]
                    
                    if text[line].startswith("College/Department"):
                        college = text[line][text[line].index(":")+2:]
                    elif text[line].startswith("Repeat Status"):
                        repeat_status = text[line][text[line].index(":")+2:]
                    elif text[line].startswith("Restrictions"):
                        restrictions = text[line][text[line].index(":")+2:]
                    elif text[line].startswith("Prerequisites"):
                        pre_requisites = text[line][text[line].index(":")+2:]
                    elif text[line].startswith("Corequisites"):
                        co_requisites = text[line][text[line].index(":")+2:]
                
                courseInfoList.append({
                    "Course Code": course_code,
                    "Course Title": course_title,
                    "College/Department": college,
                    "Credits": credits
                })
                
                courseRestrictionsList.append({
                    "Course Code": course_code,
                    "Prerequisites": pre_requisites,
                    "Corequisites": co_requisites,
                    "Repeat Status": repeat_status,
                    "Restrictions": restrictions
                })
            print("Finished scrapping link")
        except Exception as e:
            print(e)
            print("Failed scrapping course in link:", link)
    
    print("Number of courses scrapped:",numCourses)
    
    cwd = os.getcwd()
    
    courseInfoPath = cwd + os.sep + ".." + os.sep + "mongodb" + os.sep + "data_files" + os.sep + "MongoDB-course-info.json"
    courseRestrictionsPath = cwd + os.sep + ".." + os.sep + "mongodb" + os.sep + "data_files" + os.sep + "MongoDB-course-restrictions.json"
    
    with open(courseInfoPath, "w") as jsonFile:
        json.dump(courseInfoList, jsonFile, indent=4)
    with open(courseRestrictionsPath, "w") as jsonFile:
        json.dump(courseRestrictionsList, jsonFile, indent=4)
        
        
if __name__ == "__main__":
    main()