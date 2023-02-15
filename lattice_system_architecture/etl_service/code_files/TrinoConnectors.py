import os

class TrinoConnector:
    
    def createConnector(self, newConn):
        
        name = newConn['connection_name']
        dbtype = newConn['connection_type']
        url = newConn['connection_URL']
        user = newConn['connection_username']
        password = newConn['connection_password']
        
        db = dbtype.lower()
        if db == "elasticsearch":
            self.CreateElasticsearchConnector(name, url, user, password)
        elif db == "cassandra":
            self.CreateCassandraConnector(name, url, user, password)
        elif db == "mariadb":
            self.CreateMariadbConnector(name, url, user, password)
        elif db == "mongodb":
            self.CreateMongoConnector(name, url, user, password)
        elif db == "postgres":
            self.CreatePostgresConnector(name, url, user, password)

    def output(self, properties, connectorName):
        fileName = "/catalog/" + connectorName + ".properties"
        with open(fileName, "w") as f:
            for line in properties:
                f.write(line+"\n")
        f.close()

    def CreateElasticsearchConnector(self, name, url, user, password):
        properties = []
        splitURL = url.split(":")

        properties.append(f"connector.name=elasticsearch")
        properties.append(f"elasticsearch.host={splitURL[0]}")
        properties.append(f"elasticsearch.port={splitURL[1]}")
        properties.append(f"elasticsearch.auth.user={user}")
        properties.append(f"elasticsearch.auth.password={password}")
        properties.append("elasticsearch.default-schema-name=default")

        self.output(properties, name)

    def CreateCassandraConnector(self, name, url, user, password):
        properties = []
        splitURL = url.split(":")

        properties.append(f"connector.name=cassandra")
        properties.append(f"cassandra.contact-points={splitURL[0]}")
        properties.append(f"cassandra.native-protocol-port={splitURL[1]}")
        properties.append(f"cassandra.username={user}")
        properties.append(f"cassandra.password={password}")
        properties.append("cassandra.load-policy.dc-aware.local-dc=datacenter1")

        self.output(properties, name)

    def CreateMariadbConnector(self, name, url, user, password):
        properties = []
        concatenatedURL = f"jdbc:mariadb://{url}"

        properties.append(f"connector.name=mariadb")
        properties.append(f"connection-url={concatenatedURL}")
        properties.append(f"connection-user={user}")
        properties.append(f"connection-password={password}")

        self.output(properties, name)

    def CreateMongoConnector(self, name, url, user=None, password=None):
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

        properties.append(f"connector.name=mongodb")
        properties.append(f"mongodb.connection-url={concatenatedURL}")

        self.output(properties, name)

    def CreatePostgresConnector(self, name, url, user, password):
        properties = []

        properties.append(f"connector.name=postgresql")
        properties.append(f"connection-url={url}")
        properties.append(f"connection-user={user}")
        properties.append(f"connection-password={password}")

        self.output(properties, name)

if __name__ == "__main__":
    # Testing
    trinoConnectors = TrinoConnectors()
    trinoConnectors.CreateElasticsearchConnector("localhost:9200", "elastic", "lakjsdf982")
    trinoConnectors.CreateCassandraConnector("localhost:9142", "user", "asdfasdg3g2344")
    trinoConnectors.CreateMariadbConnector("jdbc:mariadb://mariadb:3306", "mariauser", "asdxcvbesxfgh")
    trinoConnectors.CreateMongoConnector("mongodb://mongouser:mongopassword@sample.host:27017/")
    trinoConnectors.CreatePostgresConnector("jdbc:postgresql://example.net:5432/database", "postgres", "ikjhfsgioeduy")