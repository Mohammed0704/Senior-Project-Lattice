from langchain.chat_models import ChatOpenAI
from langchain.chains import GraphCypherQAChain
from langchain.graphs import Neo4jGraph

#pip3 install neo4j openai langchain #may need to run as Admin

graph = Neo4jGraph(
    url="bolt://localhost:7687", 
    username="neo4j", 
    password="password"
)

import os

os.environ['OPENAI_API_KEY'] = "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"

chain = GraphCypherQAChain.from_llm(
    ChatOpenAI(temperature=0), graph=graph, verbose=True,
)

chain.run("""
What employees teach the Class CS 171?
""")