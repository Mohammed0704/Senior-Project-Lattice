#!/usr/bin/env bash

#copy cassandra data into the cassandra container
docker cp ./cassandra/data_files cassandra:/

docker exec -it cassandra cqlsh -e "DROP KEYSPACE finances;"
docker exec -it cassandra cqlsh -e "CREATE KEYSPACE finances WITH REPLICATION = { 'class' : 'NetworkTopologyStrategy', 'datacenter1' : 3 };"

#employee_salaries
docker exec -it cassandra cqlsh -e "CREATE TABLE finances.employee_salaries(
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
                                    );"

docker exec -it cassandra cqlsh -e "COPY finances.employee_salaries (drexel_id, annual_salary, date_of_birth, full_name, job_title, year_started, employer, time_reporting_period, direct_deposit, electronic_w2_form, turbo_tax_option) 
                FROM '/data_files/Cassandra-employee_salaries.csv' 
                WITH HEADER = TRUE;"


#health_insurance
docker exec -it cassandra cqlsh -e "CREATE TABLE finances.health_insurance(
                                    drexel_id text PRIMARY KEY, 
                                    waived boolean, 
                                    provider text,
                                    deductible varint,
                                    maximum_coverage_amount varint
                                    );"

docker exec -it cassandra cqlsh -e "COPY finances.health_insurance (drexel_id, waived, provider, deductible, maximum_coverage_amount) 
                FROM '/data_files/Cassandra-health_insurance.csv' 
                WITH HEADER = TRUE;"

