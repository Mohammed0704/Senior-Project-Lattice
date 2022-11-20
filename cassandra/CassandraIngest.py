from cassandra.cluster import Cluster
import csv
import os

currentDirectory = os.getcwd()

cluster = Cluster(["localhost"], port=9042)
session = cluster.connect()

try:
    session.execute("DROP KEYSPACE finances")
except:
    pass

session.execute("CREATE KEYSPACE finances WITH REPLICATION = { 'class' : 'NetworkTopologyStrategy', 'datacenter1' : 3 }")
session.execute("USE finances")

session.execute('''CREATE TABLE employee_salaries(
    drexel_id text PRIMARY KEY, 
    annual_salary varint, 
    date_of_birth text,
    full_name text,
    job_title text,
    year_started varint,
    employer text,
    time_reporting_period text,
    direct_deposit boolean,
    electronic_w2_form boolean,
    turbo_tax_option text
    )'''
)

with open(currentDirectory + "/cassandra/Cassandra-employee_salaries.csv", "r") as csvFile:
    reader = csv.reader(csvFile)
    next(csvFile)

    for row in reader:
        insertValues = "("
        for column in row:
            isNumber = False
            try:
                castedColumn = int(column)
                isNumber = True
            except:
                if column.lower() == "true" or column.lower() == "false":
                    insertValues = insertValues + column + ", "
                elif type(column) == str:
                    insertValues = insertValues + "\'" + column + "\', "
            if (isNumber):
                insertValues = insertValues + column + ", "
        insertValues = insertValues[:-2] + ")"

        insertHeaders = "(drexel_id, annual_salary, date_of_birth, full_name, job_title, year_started, employer, time_reporting_period, direct_deposit, electronic_w2_form, turbo_tax_option)"
        session.execute("INSERT INTO finances.employee_salaries " + insertHeaders + " VALUES " + insertValues)