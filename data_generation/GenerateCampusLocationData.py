import csv
import os

currentDirectory = os.getcwd()

#Postgres.campus_life.locations
buildingName = ""
description = ""
address = ""
phone = ""
email = ""
website = ""
zipCode = 0
campus = ""
signInRequired = False
studentAccessible = False

campusLocationHeaders = ["Building Name", "Description", "Address", "Phone", "Email", "Website", "Zip Code", "Campus", "Sign In Required", "Student Accessible"]
campusLocationRows = []

campusLocationRows.append(["W. W. Hagerty Library", "Founded in 1983, W.W. Hagerty Library houses nearly half a million of books, periodicals, DVDs, videos and archival materials.",
                            "3300 Market St, Philadelphia, PA 19104", "215-895-1500", "liaisons@drexel.libanswers.com", "https://www.library.drexel.edu/",
                            19104, "University City", True, True])

campusLocationRows.append(["Math Resource Center", "The Math Resource Center is available to Drexel University students who need assistance in undergraduate math courses offered by the Department of Mathematics.",
                            "15 S. 33rd St. Room 207", "", "sp955@drexel.edu", "https://drexel.edu/coas/academics/departments-centers/mathematics/math-resource-center/",
                            19104, "University City", True, True])

campusLocationRows.append(["Drexel Recreation Center", "Opened in February 2010, the state-of-the-art Drexel Recreation Center is the fitness hub in University City. The Recreation Center is committed to providing a lasting and meaningful impact on the health and well-being of its members. The center serves as a symbol of Drexel University's commitment to the health of the community—both in body and mind.",
                            "Recreation Center 33rd and Market Streets", "215-571-3830", "memberships@drexel.edu", "https://drexel.edu/recathletics/reccenter/overview/",
                            19104, "University City", True, True])

campusLocationRows.append(["Barnes & Noble Drexel University", "Shop Drexel University Bookstore for men's, women's and children's apparel, gifts, textbooks, and more.",
                            "3250 Chestnut St, Philadelphia, PA 19104", "215-895-2860", "", "https://drexel.bncollege.com/",
                            19104, "University City", False, True])

campusLocationRows.append(["Handschumacher Dining Center", "One of the dining centers available for Drexel students.",
                            "3201 Chestnut St, Philadelphia, PA 19104", "215-895-2860", "", "https://drexel.campusdish.com/en/LocationsAndMenus/HandschumacherDiningCenter",
                            19104, "University City", True, True])

campusLocationRows.append(["Urban Eatery", "One of the dining centers available for Drexel students.",
                            "3400 Lancaster Ave, Philadelphia, PA 19104", "", "campusdining@drexel.edu", "https://drexel.campusdish.com/LocationsAndMenus/UrbanEatery",
                            19104, "University City", True, True])

campusLocationRows.append(["Korman Center", "The Korman Center houses IT's professional staff as well as the Instructional Technology center.",
                            "15 S. 33rd St.", "", "", "",
                            19104, "University City", False, True])

campusLocationRows.append(["Daskalakis Athletic Center", "The Daskalakis Athletic Center (DAC) is the home of Drexel Athletics. The facility includes a swimming pool located on the lower level, five squash courts, a golf center, and a gymnasium featuring courts for recreational, intramural, club volleyball, and basketball. The DAC primarily services varsity sports.",
                            "3301 Market St, Philadelphia, PA 19104", "215-895-1977", "Recathletics@drexel.edu", "https://drexel.edu/recathletics/",
                            19104, "University City", True, True])

campusLocationRows.append(["Academic Building", "",
                            "3141 Chestnut St, Philadelphia, PA 19104", "", "", "https://www.lebow.drexel.edu/about/campuses/location/academic-building?page=1",
                            19104, "University City", False, True])

campusLocationRows.append(["Constantine N. Papadakis Integrated Sciences Building", "The College of Arts and Sciences’ Gold LEED-certified Papadakis Integrated Sciences Building is home to North America’s largest living biowall - and the only wall of its kind in a U.S. university. The landmark facility is named in honor of Drexel’s 12th president, Constantine N. Papadakis, PhD. During his tenure, Papadakis recognized the need for greater space to serve the biomedical sciences, a field that quickly flourished after the University’s merger with the College of Medicine.",
                            "3245 Chestnut St, Philadelphia, PA 19104", "", "", "https://drexel.edu/coas/academics/departments-centers/biology/Papadakis-Integrated-Sciences-Building/",
                            19104, "University City", False, True])

campusLocationRows.append(["Curtis Hall", "Funded by a Cyrus Hermann Kotzschmar Curtis (publisher of the Ladies' Home Journal and the Saturday Evening Post). The initial three-story concrete and steel structure was built to accommodate four more stories in the future. It provided laboratory and classroom spaces for mechanical, civil, chemical, and electrical engineering as well as a gymnasium on the top floor which included a rifle range and rooftop baseball cage and running track. Curtis also purchased the land adjacent to the site to ensure abundant natural light into the structure.",
                            "3141 Chestnut St Ste 301, Philadelphia, PA 19104", "", "", "",
                            19104, "University City", False, True])

campusLocationRows.append(["Randell Hall", "Called East Hall until 1924 when renamed for Lillie Randell and Letitia Garrison, sisters, donated money to the Institute.",
                            "3141 Chestnut St Ste 301, Philadelphia, PA 19104", "", "", "",
                            19104, "University City", False, True])

campusLocationRows.append(["Disque Hall", "",
                            "32 South 32nd Street, Philadelphia, PA", "", "", "",
                            19104, "University City", False, True])           

campusLocationRows.append(["Gerri C. LeBow Hall", "",
                            "3220 Market St. Philadelphia, PA 19104", "215-895-2111", "lcbdeansoffice@drexel.edu", "https://www.lebow.drexel.edu/about",
                            19104, "University City", False, True])          

campusLocationRows.append(["Gerri C. LeBow Hall", "",
                            "3220 Market St. Philadelphia, PA 19104", "215-895-2111", "lcbdeansoffice@drexel.edu", "https://www.lebow.drexel.edu/about",
                            19104, "University City", False, True])  



#Postgres.campus_life.locations
with open(currentDirectory + "/Postgres_Data/Postgres-locations.csv", 'w', newline='') as csvfile: 
    csvwriter = csv.writer(csvfile) 
    csvwriter.writerow(campusLocationHeaders)         
    csvwriter.writerows(campusLocationRows)