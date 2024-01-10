"""
"""
from dotenv import load_dotenv
load_dotenv()

import create_graph
import create_embeddings
import create_search_index
import neo4j_qa
import vector_search


steps = [
    # This step requires csv files to be stored in Import location of Neo4j Desktop
    # 'create_graph',

    # You can skip this step if you use embeddings file provided with the project
    # 'create_embeddings',

    # Requires embeddings.csv file to be stored in import location for Neo4j
    # 'create_search_index',

   # Query database schema
   # 'neo4j_qa',

    # Query vector index
    'vector_search',

]

def go():

    if 'create_graph' in steps:
        create_graph.go()

    if 'create_embeddings' in steps:
        create_embeddings.go()

    if 'create_search_index' in steps:
        create_search_index.go()

    if 'neo4j_qa' in steps:
        neo4j_qa.go()

    if 'vector_search' in steps:
        vector_search.go()

if __name__ == '__main__':
    go()