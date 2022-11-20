from elasticsearch import Elasticsearch

class Elastic:
    
    def __init__(self):
        self.es = Elasticsearch(["http://localhost:9200"])
        
    def createIndex(self, indexName):
        returnString = self.es.indices.create(index=indexName, ignore=400, body={
            "mappings": {
                "properties": {
                    "drexelid": {
                        "type": "text",
                        "fields": {
                            "keyword": {
                                "type": "keyword",
                                "ignore_above": 16
                            }
                        }
                    },
                    "name": {
                        "type": "text",
                        "ignore_above": 128
                    },
                    "action": {
                        "type": "text",
                        "ignore_above": 64
                    },
                    "date": {
                        "type": "date",
                        "format": "MM/dd/yyyy"
                    },
                    "time": {
                        "type": "date",
                        "format": "HH:mm:ss"
                    },
                    "location": {
                        "type": "text",
                        "ignore_above": 64
                    }
                }
            }
        })
        print(returnString)
    
    def deleteIndex(self, indexName):
        print(self.es.indices.delete(index=indexName, ignore=400))
    
    def post(self, indexName, drexelid, name, action, date, time, location):
        returnString = self.es.index(index=indexName, document={
            "drexelid": drexelid,
            "name": name,
            "action": action,
            "date": date,
            "time": time,
            "location": location
        })
        print(returnString)
    
    def get(self, indexName, drexelid):
        returnString = self.es.search(index=indexName, query={
            "match_phrase": {
                "drexelid": {
                    "query": drexelid
                }
            }
        })
        print(returnString)

if __name__ == "__main__":
    '''
    This is the initial interface to elasticsearch, very bare bones at the moment, but I tested it and it does indeed work.
    There are many deprecation warnings due to changes in the Elasticsearch package that I haven't looked into yet, but
    this is a start for now.
    
    TODO:
        1. Look into deprecation warnings further and update code accordingly 
        2. Create separate methods for the different table schemas that we have for our elasticsearch tables
    '''
    
    es = Elastic()
    
    index = "gymlog"
    es.createIndex(index)
    es.post(index, "ves35", "Vincent Savarese", "signed-in", "11/20/2022", "09:30:00", "gym")
    es.get(index, "ves35")
    es.deleteIndex(index)