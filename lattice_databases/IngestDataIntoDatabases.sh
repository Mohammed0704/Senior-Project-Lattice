#!/usr/bin/env bash

python ./elasticsearch/ElasticFileConversion.py

./cassandra/IngestCassandraData.sh
RESULT=$?
if [ $RESULT -eq 0 ]; then
    echo -e "\nData successfully ingested into Cassandra!"
else
    echo -e "\nData failed to ingest into Cassandra! Exiting..."
    exit 1
fi

./mariadb/IngestMariaDBData.sh
RESULT=$?
if [ $RESULT -eq 0 ]; then
    echo -e "\nData successfully ingested into MariaDB!"
else
    echo -e "\nData failed to ingest into MariaDB! Exiting..."
    exit 1
fi

./postgres/IngestPostgresData.sh
RESULT=$?
if [ $RESULT -eq 0 ]; then
    echo -e "\nData successfully ingested into Postgres!"
else
    echo -e "\nData failed to ingest into Postgres! Exiting..."
    exit 1
fi

./mongodb/IngestMongoData.sh
RESULT=$?
if [ $RESULT -eq 0 ]; then
    echo -e "\nData successfully ingested into Mongo!"
else
    echo -e "\nData failed to ingest into Mongo! Exiting..."
    exit 1
fi

./elasticsearch/IngestElasticsearchData.sh
RESULT=$?
if [ $RESULT -eq 0 ]; then
    echo -e "\nData successfully ingested into Elasticsearch!"
else
    echo -e "\nData failed to ingest into Elasticsearch! Exiting..."
    exit 1
fi