from neo4j import GraphDatabase
from langchain.embeddings.sentence_transformer import SentenceTransformerEmbeddings
from langchain_community.embeddings import OpenAIEmbeddings


########### Neo4j ###########
"""                                                                                                 
Initiate the Neo4j Driver                                                                           
"""
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


########### Embeddings & LLMs ###########
def _embedding_function():
    """Initiate embedding function"""
    # size: 384
    embedding_model_name = 'all-MiniLM-L6-v2'
    return SentenceTransformerEmbeddings(model_name=embedding_model_name)

def _embedding_function_openai():
    # size: 1536
    return OpenAIEmbeddings()


########### Supportive functions ###########
def load_cypher_queries(file_path):
    queries = []
    with open(file_path, 'r') as file:
        for line in file:
            # Strip whitespace
            line = line.strip()

            # Check if line is empty or starts with //
            if not line or line.startswith('//'):
                continue

            # Add the line to the list of queries
            queries.append(line)
    return queries
