"""
Udemy training PROJECT
"""

import create_graph
import create_embeddings
import create_search_index
import neo4j_qa
import vector_search

# Define the steps to be executed
steps = [
    # This step requires csv files to be accessible for AuraDB
    # 'create_graph',

    # You can skip this step if you use embeddings file provided with the project
    # 'create_embeddings',

    # Requires embeddings.csv file to be stored in import location for Neo4j
    # 'create_search_index',

    # Query database schema
    # 'neo4j_qa',

    # Query vector index
    # 'vector_search',
]

def execute_steps(steps_to_execute):
    if 'create_graph' in steps_to_execute:
        create_graph.go()

    if 'create_embeddings' in steps_to_execute:
        create_embeddings.go()

    if 'create_search_index' in steps_to_execute:
        create_search_index.go()

    if 'neo4j_qa' in steps_to_execute:
        neo4j_qa.go()

    if 'vector_search' in steps_to_execute:
        vector_search.go()

if __name__ == '__main__':
    execute_steps(steps)
