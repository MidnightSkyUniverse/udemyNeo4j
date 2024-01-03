from dotenv import load_dotenv
load_dotenv()
import os

from langchain.prompts import PromptTemplate
from langchain.agents import AgentType, initialize_agent
from langchain.tools import Tool
from langchain.chains import RetrievalQA
from langchain.chat_models.openai import ChatOpenAI
from langchain.vectorstores.neo4j_vector import Neo4jVector
from langchain.graphs import Neo4jGraph
from langchain.chains import GraphCypherQAChain



from utils import _embedding_function


### VECTOR INDEX SEARCH ###
def define_vector_retrieval():
    pass


def retriever_qa(query):
    """Retreiver QA"""
    retrievalQA = define_vector_retrieval()
    results = retrievalQA({"query": query})

    return str(results)

### SCHEMA SEARCH  ###

def define_schema_chain():
    pass

def schema_qa(query):
    """Retreiver QA"""
    retrievalQA = define_schema_chain()
    results = retrievalQA.run(query)

    return str(results)


tools = []

def go():
    llm = ChatOpenAI()

    agent = initialize_agent(
        tools, llm,
        agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
        max_iterations=3,
        verbose=True,
        handle_parsing_errors=True,
    )

    while True:
        q = input("> ")
        print(agent.run(q))

if __name__ =='__main__':
    go()