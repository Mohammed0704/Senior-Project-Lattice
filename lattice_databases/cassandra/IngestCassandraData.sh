#!/usr/bin/env bash

windowsDir=/c/'Program Files'
if [ -d "$windowsDir" ]; then #checks if the machine is Windows and provides alternate commands if so

    #copy cassandra data into the cassandra container
    docker cp ./cassandra/data_files cassandra:/

    winpty docker exec -it cassandra cqlsh -e "DROP KEYSPACE IF EXISTS finances;"
    winpty docker exec -it cassandra cqlsh -e "CREATE KEYSPACE finances WITH REPLICATION = { 'class' : 'NetworkTopologyStrategy', 'datacenter1' : 3 };"

    #employee_salaries
    winpty docker exec -it cassandra cqlsh -e "CREATE TABLE finances.employee_salaries(
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

    winpty docker exec -it cassandra cqlsh -e "COPY finances.employee_salaries (drexel_id, annual_salary, date_of_birth, full_name, job_title, year_started, employer, time_reporting_period, direct_deposit, electronic_w2_form, turbo_tax_option) 
                    FROM '/data_files/Cassandra-employee_salaries.csv' 
                    WITH HEADER = TRUE;"


    #health_insurance
    winpty docker exec -it cassandra cqlsh -e "CREATE TABLE finances.health_insurance(
                                        drexel_id text PRIMARY KEY, 
                                        waived boolean, 
                                        provider text,
                                        deductible varint,
                                        maximum_coverage_amount varint
                                        );"

    winpty docker exec -it cassandra cqlsh -e "COPY finances.health_insurance (drexel_id, waived, provider, deductible, maximum_coverage_amount) 
                    FROM '/data_files/Cassandra-health_insurance.csv' 
                    WITH HEADER = TRUE;"


    #housing_costs
    winpty docker exec -it cassandra cqlsh -e "CREATE TABLE finances.housing_costs(
                                        residence_name text PRIMARY KEY, 
                                        room_style text, 
                                        eligible_residents text,
                                        minimum_monthly_cost varint,
                                        maximum_monthly_cost varint
                                        );"

    winpty docker exec -it cassandra cqlsh -e "COPY finances.housing_costs (residence_name, room_style, eligible_residents, minimum_monthly_cost, maximum_monthly_cost) 
                    FROM '/data_files/Cassandra-housing-costs.csv' 
                    WITH HEADER = TRUE;"


    #overhead_costs
    winpty docker exec -it cassandra cqlsh -e "CREATE TABLE finances.overhead_costs(
                                        name_of_building text PRIMARY KEY, 
                                        monthly_electricity varint, 
                                        monthly_heating varint,
                                        monthly_water varint,
                                        monthly_additional_utilities varint
                                        );"

    winpty docker exec -it cassandra cqlsh -e "COPY finances.overhead_costs (name_of_building, monthly_electricity, monthly_heating, monthly_water, monthly_additional_utilities) 
                    FROM '/data_files/Cassandra-overhead-costs.csv' 
                    WITH HEADER = TRUE;"


    #software_costs
    winpty docker exec -it cassandra cqlsh -e "CREATE TABLE finances.software_costs(
                                        software text PRIMARY KEY, 
                                        drexel_annual_license_cost varint
                                        );"

    winpty docker exec -it cassandra cqlsh -e "COPY finances.software_costs (software, drexel_annual_license_cost) 
                    FROM '/data_files/Cassandra-software_costs.csv' 
                    WITH HEADER = TRUE;"


    #tuition
    winpty docker exec -it cassandra cqlsh -e "CREATE TABLE finances.tuition(
                                        drexel_id text PRIMARY KEY, 
                                        year varint, 
                                        tuition_and_fees float,
                                        annual_financial_aid_award float,
                                        subsidized_loan_offered float,
                                        unsubsidized_loan_offered float,
                                        accepted_subsidized boolean,
                                        accepted_unsubsidized boolean,
                                        outstanding_balances float
                                        );"

    winpty docker exec -it cassandra cqlsh -e "COPY finances.tuition (drexel_id, year, tuition_and_fees, annual_financial_aid_award, subsidized_loan_offered, unsubsidized_loan_offered, accepted_subsidized, accepted_unsubsidized, outstanding_balances) 
                    FROM '/data_files/Cassandra-tuition.csv' 
                    WITH HEADER = TRUE;"
else
    #copy cassandra data into the cassandra container
    docker cp ./cassandra/data_files cassandra:/

    docker exec -it cassandra cqlsh -e "DROP KEYSPACE IF EXISTS finances;"
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


    #housing_costs
    docker exec -it cassandra cqlsh -e "CREATE TABLE finances.housing_costs(
                                        residence_name text PRIMARY KEY, 
                                        room_style text, 
                                        eligible_residents text,
                                        minimum_monthly_cost varint,
                                        maximum_monthly_cost varint
                                        );"

    docker exec -it cassandra cqlsh -e "COPY finances.housing_costs (residence_name, room_style, eligible_residents, minimum_monthly_cost, maximum_monthly_cost) 
                    FROM '/data_files/Cassandra-housing-costs.csv' 
                    WITH HEADER = TRUE;"


    #overhead_costs
    docker exec -it cassandra cqlsh -e "CREATE TABLE finances.overhead_costs(
                                        name_of_building text PRIMARY KEY, 
                                        monthly_electricity varint, 
                                        monthly_heating varint,
                                        monthly_water varint,
                                        monthly_additional_utilities varint
                                        );"

    docker exec -it cassandra cqlsh -e "COPY finances.overhead_costs (name_of_building, monthly_electricity, monthly_heating, monthly_water, monthly_additional_utilities) 
                    FROM '/data_files/Cassandra-overhead-costs.csv' 
                    WITH HEADER = TRUE;"


    #software_costs
    docker exec -it cassandra cqlsh -e "CREATE TABLE finances.software_costs(
                                        software text PRIMARY KEY, 
                                        drexel_annual_license_cost varint
                                        );"

    docker exec -it cassandra cqlsh -e "COPY finances.software_costs (software, drexel_annual_license_cost) 
                    FROM '/data_files/Cassandra-software_costs.csv' 
                    WITH HEADER = TRUE;"


    #tuition
    docker exec -it cassandra cqlsh -e "CREATE TABLE finances.tuition(
                                        drexel_id text PRIMARY KEY, 
                                        year varint, 
                                        tuition_and_fees float,
                                        annual_financial_aid_award float,
                                        subsidized_loan_offered float,
                                        unsubsidized_loan_offered float,
                                        accepted_subsidized boolean,
                                        accepted_unsubsidized boolean,
                                        outstanding_balances float
                                        );"

    docker exec -it cassandra cqlsh -e "COPY finances.tuition (drexel_id, year, tuition_and_fees, annual_financial_aid_award, subsidized_loan_offered, unsubsidized_loan_offered, accepted_subsidized, accepted_unsubsidized, outstanding_balances) 
                    FROM '/data_files/Cassandra-tuition.csv' 
                    WITH HEADER = TRUE;"
fi