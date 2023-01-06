#!/usr/bin/env bash

curl -X DELETE 'http://localhost:9200/areas_of_study'
curl -X DELETE 'http://localhost:9200/departments'
curl -X DELETE 'http://localhost:9200/programs'

curl -X DELETE 'http://localhost:9200/hagerty_library_logs'
curl -X DELETE 'http://localhost:9200/recreation_center_logs'
curl -X DELETE 'http://localhost:9200/systems_logs'

curl -H 'Content-Type: application/json' -X POST 'localhost:9200/_bulk?pretty' --data-binary @./elasticsearch/data_files/Elasticsearch-additional_area_of_study.json
curl -H 'Content-Type: application/json' -X POST 'localhost:9200/_bulk?pretty' --data-binary @./elasticsearch/data_files/Elasticsearch-drexel_additional_education_info-departments.json
curl -H 'Content-Type: application/json' -X POST 'localhost:9200/_bulk?pretty' --data-binary @./elasticsearch/data_files/Elasticsearch-programs.json

curl -H 'Content-Type: application/json' -X POST 'localhost:9200/_bulk?pretty' --data-binary @./elasticsearch/data_files/logs/LibraryLogs.json
curl -H 'Content-Type: application/json' -X POST 'localhost:9200/_bulk?pretty' --data-binary @./elasticsearch/data_files/logs/RecreationCenterLogs.json
curl -H 'Content-Type: application/json' -X POST 'localhost:9200/_bulk?pretty' --data-binary @./elasticsearch/data_files/logs/SystemsLogs.json