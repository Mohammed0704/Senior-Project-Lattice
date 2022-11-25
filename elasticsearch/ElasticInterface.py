from elasticsearch import Elasticsearch, NotFoundError

class Elastic:
    
    def __init__(self):
        self.es = Elasticsearch(hosts=["http://localhost:9200"], basic_auth=('elastic', 'Aouf7oHRS6pac2frrC5a'))
        
    def createIndex(self, indexName: str, properties: list):
        mappings={ "properties": {} }
        for prop in properties:
            mappings["properties"][prop[0]] = prop[1]
        return self.es.indices.create(index=indexName, ignore=400, mappings=mappings)
    
    def deleteIndex(self, indexName):
        try:
            return self.es.indices.delete(index=indexName, ignore=400)
        except NotFoundError as e:
            return e
    
    def post(self, indexName, doc):
        return self.es.index(index=indexName, document=doc)
        
    
    def get(self, indexName, drexelid):
        returnString = self.es.search(index=indexName, query={
            "match_phrase": {
                "drexelid": {
                    "query": drexelid
                }
            }
        })
        return returnString
    