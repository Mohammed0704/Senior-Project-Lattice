import os

CWD = os.getcwd()

def output(properties, connectorName):
    fileName = CWD + os.sep + connectorName + ".properties"
    with open(fileName, "w") as f:
        for line in properties:
            f.write(line+"\n")
    f.close()

def CreateElasticsearchConnector(url, user, password):
    properties = []
    splitURL = url.split(":")

    properties.append("connector.name=elasticsearch")
    properties.append(f"elasticsearch.host={splitURL[0]}")
    properties.append(f"elasticsearch.port={splitURL[1]}")
    properties.append(f"elasticsearch.auth.user={user}")
    properties.append(f"elasticsearch.auth.password={password}")
    properties.append("elasticsearch.default-schema-name=default")

    output(properties, "elasticsearch")

def CreateCassandraConnector(url, user, password):
    properties = []
    splitURL = url.split(":")

    properties.append("connector.name=cassandra")
    properties.append(f"cassandra.contact-points={splitURL[0]}")
    properties.append(f"cassandra.native-protocol-port={splitURL[1]}")
    properties.append(f"cassandra.username={user}")
    properties.append(f"cassandra.password={password}")
    properties.append("cassandra.load-policy.dc-aware.local-dc=datacenter1")

    output(properties, "cassandra")

def CreateMariadbConnector(url, user, password):
    properties = []

    properties.append("connector.name=mariadb")
    properties.append(f"connection-url={url}")
    properties.append(f"connection-user={user}")
    properties.append(f"connection-password={password}")

    output(properties, "mariadb")

def CreateMongoConnector(url, user=None, password=None):
    properties = []

    '''
    Mongo connection url has the user and password within it in the Trino example,
    so we could change the "Create New Connection" page dynamically change it's
    input form to adjust for the nuances of each connection.  Until we decide that,
    I kept it flexible

    REF: https://trino.io/docs/current/connector/mongodb.html
    '''
    concatenatedURL = ""
    if user == None and password == None:
        concatenatedURL = url
    else:
        concatenatedURL = f"mongodb://{user}:{password}@{url}"

    properties.append("connector.name=cassandra")
    properties.append(f"mongodb.connection-url={concatenatedURL}")

    output(properties, "mongo")

def CreatePostgresConnector(url, user, password):
    properties = []

    properties.append("connector.name=postgresql")
    properties.append(f"connection-url={url}")
    properties.append(f"connection-user={user}")
    properties.append(f"connection-password={password}")

    output(properties, "postgres")

if __name__ == "__main__":
    # Testing
    CreateElasticsearchConnector("localhost:9200", "elastic", "lakjsdf982")
    CreateCassandraConnector("localhost:9142", "user", "asdfasdg3g2344")
    CreateMariadbConnector("jdbc:mariadb://mariadb:3306", "mariauser", "asdxcvbesxfgh")
    CreateMongoConnector("mongodb://mongouser:mongopassword@sample.host:27017/")
    CreatePostgresConnector("jdbc:postgresql://example.net:5432/database", "postgres", "ikjhfsgioeduy")