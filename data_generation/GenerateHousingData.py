from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

'''
The two Python packages required here are "selenium" and "Webdriver_manager" which you can download simply using 
$pip install <package> 

Here's the Selenium docs for reference: https://selenium-python.readthedocs.io
'''

import time
import csv
import os

def driverSetup():
    # This can be used to add additional options like a download path if you wanted your web scrapper to hit a button and download a file on a website 
    options = Options()
    options.headless = True # If false, the browser window will pop up
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    return driver

def createHousingCostsList(driver):
    housingCosts = []
    
    driver.get("https://drexel.edu/drexelcentral/cost/housing/") # This is how you navigate to sites
    
    '''
    This next operation is important, this is how you find element(s) in the HTML.
        When on a website, you can right click and inspect element, and there you can see where that element is in the HTML
        Now, you can search for things by their different attributes (if they have them) like:
            By.CLASS_NAME
            By.ID
            By.CSS_SELECTOR
            By.XPATH
        In this case, there were no class names or IDs to go by, so I used XPATH
        The way to get an HTML element's XPATH is to inspect the HTML on the page, right click the element you want, hover on the "Copy" option, then 
            either choose "Copy XPath" for a relative XPATH (like the one right below), or "Copy full XPath" for an absolute XPATH from the initial HTML tag. 
    '''
    housingCostsTable = driver.find_element(By.XPATH, '//*[@id="center-rail"]/article/div[1]/table[1]/tbody')
    
    '''
    For this next operation, if you look at the HTML on the page, there is a tbody element and a bunch of tr (table rows) elements inside it.
    So, once we have the tbody element stored in the varibale housingCostsTable, we can use that as an anchor to gather all the tr's that it contains 
    using the next operation which literally reads:
        Find all the tr elements inside of the tbody element and store them in a list
    '''
    housingCostsRows = housingCostsTable.find_elements(By.XPATH, ".//tr")
    
    # I'll let you figure out the rest
    header = True
    for tr in housingCostsRows:
        if header:
            header = False
            continue
        housingCost = []
        tds = tr.find_elements(By.XPATH, ".//td")
        for td in tds:
            # The text came with a lot of unnecessary characters, so this is just filtering them out
            string = td.get_attribute("textContent").strip(r"[ ]*")
            string = string.replace(u'\xa0', u'')
            string = string.replace(u'\n', u'')
            if "$" in string:
                string = string.replace(u'$', u'')
                string = string.replace(u',', u'')
                string = int(int(string) / 3)
            housingCost.append(string)
        housingCosts.append(housingCost)
    
    return housingCosts

def createHousingOptionsList(residencies):
    housingOptions = []
    
    # On Drexel's housing cost page, the cost for each residence is listed as "Quarterly Cost", so I put that in as is and divide it by three 
    # to approximate the monthly cost
    housingOptions.append([residencies[0], "3301 Arch Street Philadelphia, PA 19104", "215.571.3080", "Drexel", False, True, "https://drexel.edu/studentlife/campus-living/housing/options"])
    housingOptions.append([residencies[1], "115 N. 32nd Street Philadelphia, PA 19104", "215.571.3179", "Drexel", False, True, "https://drexel.edu/studentlife/campus-living/housing/options"])
    housingOptions.append([residencies[2], "223 N. 34th Street Philadelphia, PA 19104", "215.571.3150", "Drexel", False, True, "https://drexel.edu/studentlife/campus-living/housing/options"])
    housingOptions.append([residencies[3], "3200 Race Street Philadelphia, PA 19104", "215.571.3087", "Drexel", False, True, "https://drexel.edu/studentlife/campus-living/housing/options"])
    housingOptions.append([residencies[4], "3300 Race Street Philadelphia, PA 19104", "215.571.3103", "Drexel", False, True, "https://drexel.edu/studentlife/campus-living/housing/options"])
    housingOptions.append([residencies[5], "101 N 34th Street Philadelphia, PA 19104", "215.571.3028", "Drexel", False, True, "https://drexel.edu/studentlife/campus-living/housing/options"])
    housingOptions.append([residencies[6], "3320 Powelton Avenue Philadelphia, PA 19104", "215.571.3068", "Drexel", False, True, "https://drexel.edu/studentlife/campus-living/housing/options"])
    housingOptions.append([residencies[7], "325 N. 15th Street Philadelphia, PA 19102", "215.571.4410", "Drexel", False, True, "https://drexel.edu/studentlife/campus-living/housing/options"])
    housingOptions.append([residencies[8], "3200 Chestnut Street Philadelphia, PA 19104", "(215) 243-3555", "American Campus Communities", True, True, "https://www.americancampus.com/student-apartments/pa/philadelphia/chestnut-square"])
    housingOptions.append([residencies[9], "3400 Lancaster Avenue Philadelphia, PA 19104", "(215) 222-3100", "American Campus Communities", True, True, "https://www.americancampus.com/student-apartments/pa/philadelphia/the-summit-at-university-city#amenities"])
    housingOptions.append([residencies[10], "3175 John F Kennedy Boulevard Philadelphia, PA 19104", "(215) 382-3432", "American Campus Communities", True, True, "https://www.americancampus.com/student-apartments/pa/philadelphia/university-crossings"])

    return housingOptions

def main():
    
    '''
    (Structure)
    Database System:
        Database:
            Table:
                Fields
    
    https://drexel.edu/drexelcentral/cost/housing/
    Cassandra:
        finances:
            housing_costs:
                residence_name
                eligible_residents
                room_style
                Monthly Cost 

    https://drexel.edu/studentlife/campus-living/housing/options
    https://drexel.edu/studentlife/campus-living/housing/options/affiliated-housing
    Postgres:
        campus_life:
            housing_options
                residence_name
                address
                front_desk_phone
                owner
                is_affliated_housing
                on_campus
                url
    '''
    
    driver = driverSetup()
    
    housingOptionsHeaders = ["Residence Name", "Is Affiliated Housing", "Address", "Owner", "On Campus"]
    housingCostsHeaders = ["Residence Name", "Eligible Residents", "Room Style", "Monthly Cost"]
    residencies = ["Bentley Hall", "Caneris Hall", "Millenium Hall", "North Hall", "Race Street Residences", "Towers Hall", 
                    "Van Rensselaer", "Stiles Hall", "Chestnut Square", "The Summit", "University Crossings"]
    
    housingOptions = createHousingOptionsList(residencies)
    housingCosts = createHousingCostsList(driver)
    
    cwd = os.getcwd()
    
    with open(cwd + "/Postgres_Data/Postgres-housing-costs.csv", 'w', newline='') as csvfile: 
        csvwriter = csv.writer(csvfile) 
        csvwriter.writerow(housingCostsHeaders)         
        csvwriter.writerows(housingCosts)
    
    with open(cwd + "/Postgres_Data/Postgres-housing-options.csv", 'w', newline='') as csvfile: 
        csvwriter = csv.writer(csvfile) 
        csvwriter.writerow(housingOptionsHeaders)         
        csvwriter.writerows(housingOptions)

if __name__ == "__main__":
    main()