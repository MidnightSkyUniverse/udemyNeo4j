"""
    Test search on vector index
"""
from langchain.chains import RetrievalQA
from langchain_openai import ChatOpenAI
from langchain.vectorstores.neo4j_vector import Neo4jVector
from dotenv import load_dotenv
import os

from utils import _embedding_function


def go():

    url = os.getenv('NEO4J_URI')
    username = os.getenv('NEO4J_USERNAME')
    password = os.getenv('NEO4J_PASSWORD')





if __name__=='__main__':
    go()