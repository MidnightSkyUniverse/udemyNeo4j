from neo4j import GraphDatabase
from langchain.embeddings.sentence_transformer import SentenceTransformerEmbeddings
from langchain.embeddings import OpenAIEmbeddings


########### Neo4j ###########
"""                                                                                                 
Initiate the Neo4j Driver                                                                           
"""
# tag::initDriver[]
def init_driver(uri, username, password):
    pass

"""                                                                                                 
If the driver has been instantiated, close it and all remaining open sessions                       
"""
def close_driver(driver: GraphDatabase):
    pass

def clean_up_database(driver):
   pass

def execute_query(driver, query):
    pass


def load_cypher_queries(file_path):
    pass


########### Embeddings & LLMs ###########
def _embedding_function():
    """Initiate embedding function"""
    # size: 384
    embedding_model_name = 'all-MiniLM-L6-v2'
    return SentenceTransformerEmbeddings(model_name=embedding_model_name)

def _embedding_function_openai():
    # size: 1536
    return OpenAIEmbeddings()

