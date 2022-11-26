#!/usr/bin/env bash

curl -H 'Content-Type: application/json' -X POST 'localhost:9200/_bulk?pretty' --data-binary @./elasticsearch/data_files/Elasticsearch-additional_area_of_study.json

curl -H 'Content-Type: application/json' -X POST 'localhost:9200/_bulk?pretty' --data-binary @./elasticsearch/data_files/Elasticsearch-drexel_additional_education_info-departments.json

curl -H 'Content-Type: application/json' -X POST 'localhost:9200/_bulk?pretty' --data-binary @./elasticsearch/data_files/Elasticsearch-programs.json