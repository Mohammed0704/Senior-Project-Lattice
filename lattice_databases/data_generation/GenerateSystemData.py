import csv
import os
import json

currentDirectory = os.getcwd()

#CassandraDB.finances.software_costs
cassandraSoftwareCostsHeaders = ["software", "drexel_annual_license_cost"]
cassandraSoftwareCosts = []
software_name = ""
drexel_annual_license_cost = 0

#MongoDB.student_education.software
mongoSoftware = []
#software
description = ""
link = ""
licensed_by_drexel = False
license_availability = ""
student_cost_per_term = 0
software_type = ""
is_downloadable = False
operating_systems = ""
support_team = ""
support_contact = ""

#Creating the data
Systems = []
systemVars = []

##Blackboard Learn
systemVars = ["Blackboard Learn",
              160000,
              "Drexel's platform for online course delivery and management software. Instructors can use Learn to deliver online course materials, or deliver completely online courses. Features discussion boards, grading tools, test administrations tools, document delivery, and much more. Students can sign in to access course materials posted by the instructor.",
              "learn.drexel.edu",
              True,
              "faculty,professional staff,students",
              0,
              "website",
              False,
              "windows,macos,linux",
              "Instructional Technology Group",
              "itg@drexel.edu"]
Systems.append(systemVars)

##ArcGIS
systemVars = ["ArcGIS",
              50000,
              "A Web-based tool from the geographic information system market leader ESRI with demographic and business data visualized in map format, as well as graphed or exportable as raw spreadsheet data.",
              "libguides.library.drexel.edu/GIS",
              True,
              "faculty,students",
              0,
              "webapp",
              False,
              "windows,macos",
              "Departmental Tech Support or IT Help Desk",
              "helpdesk@drexel.edu"]
Systems.append(systemVars)

##GIMP
systemVars = ["GIMP",
              0,
              "Image editing and manipulation program similar to Photoshop.",
              "gimp.org",
              False,
              "faculty,professional staff,students",
              0,
              "application",
              True,
              "windows,macos,linux",
              "N/A",
              "N/A"]
Systems.append(systemVars)

##Degree Works
systemVars = ["Degree Works",
              120000,
              "DegreeWorks is an online tool available to undergraduate students. DegreeWorks allows you to track your progress towards the completion of your degree program, including the number of credits you have earned and still need to complete, GPA status, and course requirements for your program. It is recommended that you use DegreeWorks in coordination with regular consultation with your academic advisor.",
              "https://drexel.edu/drexelcentral/registration/courses/degreeworks/",
              True,
              "faculty,students",
              0,
              "website",
              False,
              "N/A",
              "N/A",
              "N/A"]
Systems.append(systemVars)

##McGraw-Hill Connect
systemVars = ["McGraw-Hill Connect",
              80000,
              "An online service for instructors and strudents to streamline education.  Instructors can manage homework and quiz/exam distribution and grading; students can fill out and submit the materials the instructors provide.  Students are able to learn and watch videos on the topics as well as read the course's textbook.",
              "https://connect.mheducation.com",
              True,
              "faculty,students",
              80,
              "website",
              False,
              "N/A",
              "N/A",
              "N/A"]
Systems.append(systemVars)

##Zoom
systemVars = ["Zoom",
              20000,
              "Video-conferencing application for business meetings. Licensed at Drexel for faculty, professional staff, and students.",
              "drexel.zoom.us",
              True,
              "faculty,professional staff,students",
              0,
              "application",
              True,
              "windows,macos",
              "Video Collaboration and Production",
              "zoomadmin@drexel.edu"]
Systems.append(systemVars)

##PuTTY
systemVars = ["PuTTY",
              0,
              "Secure FTP Client.",
              "putty.org",
              False,
              "faculty,professional staff,students",
              0,
              "application",
              True,
              "windows,linux",
              "N/A",
              "N/A"]
Systems.append(systemVars)

##Tux
systemVars = ["Tux",
              0,
              "CCI maintains a compute environment to support class requirements. Typically referred to as Tux, this environment provides various services.",
              "https://www.cs.drexel.edu/~kschmidt/Ref/csLogin.html",
              False,
              "faculty,professional staff,students",
              0,
              "compute environment",
              True,
              "windows,linux,mac",
              "N/A",
              "N/A"]
Systems.append(systemVars)

for system in Systems:
  software_name = system[0]
  drexel_annual_license_cost = system[1]
  description = system[2]
  link = system[3]
  licensed_by_drexel = system[4]
  license_availability = system[5]
  student_cost_per_term = system[6]
  software_type = system[7]
  is_downloadable = system[8]
  operating_systems = system[9]
  support_team = system[10]
  support_contact = system[11]

  cassandraSoftwareCosts.append([software_name,
                                  drexel_annual_license_cost])
  
  mongoSoftware.append({"name": software_name,
                        "description": description,
                        "link": link,
                        "licensed_by_drexel": licensed_by_drexel,
                        "license_availability": license_availability,
                        "student_cost_per_term": student_cost_per_term,
                        "software_type": software_type,
                        "is_downloadable": is_downloadable,
                        "operating_systems": operating_systems,
                        "support_team": support_team,
                        "support_contact": support_contact})

#Cassandra.finances.software_costs
with open(currentDirectory + "/../cassandra/data_files/Cassandra-software_costs.csv", 'w', newline='') as csvfile: 
    csvwriter = csv.writer(csvfile) 
    csvwriter.writerow(cassandraSoftwareCostsHeaders)         
    csvwriter.writerows(cassandraSoftwareCosts)

with open(currentDirectory + "/../mongodb/data_files/MongoDB-software.json", "w") as jsonfile:
  json.dump(mongoSoftware, jsonfile, indent = 4)