#!/usr/bin/env bash

curl -X DELETE 'http://localhost:9200/areas_of_study'
curl -X DELETE 'http://localhost:9200/departments'
curl -X DELETE 'http://localhost:9200/programs'

curl -H 'Content-Type: application/json' -X POST 'localhost:9200/_bulk?pretty' --data-binary @./elasticsearch/data_files/Elasticsearch-additional_area_of_study.json
curl -H 'Content-Type: application/json' -X POST 'localhost:9200/_bulk?pretty' --data-binary @./elasticsearch/data_files/Elasticsearch-drexel_additional_education_info-departments.json
curl -H 'Content-Type: application/json' -X POST 'localhost:9200/_bulk?pretty' --data-binary @./elasticsearch/data_files/Elasticsearch-programs.json