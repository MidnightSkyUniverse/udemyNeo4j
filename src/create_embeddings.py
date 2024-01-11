"""
Create embeddings for skills in the Udemy training project
"""

import os
from dotenv import load_dotenv
import pandas as pd
from utils import (
    init_driver,
    close_driver,
    execute_query,
    _embedding_function,
)

# Constants
CSV_EMBEDDINGS_URL = 'https://raw.githubusercontent.com/MidnightSkyUniverse/udemyNeo4j/master/data/embeddings.csv'

EMBEDDING_QUERY = """
    MATCH (s:Skill)
    WHERE s.description IS NOT NULL
    RETURN s.name AS name, s.description AS description
"""

def create_skill_embeddings(driver):
    print("*** Creating skill embeddings ***")
    results = execute_query(driver, EMBEDDING_QUERY)
    df = pd.DataFrame(results)

    # Create embeddings using the imported _embedding_function
    embedding_model = _embedding_function()
    embeddings = []

    for _, row in df.iterrows():
        embedding_table = embedding_model.embed_documents([row['description']])
        embeddings.append({
            "Skill": row['name'],
            "Embedding": embedding_table[0],
        })

    embeddings_df = pd.DataFrame(embeddings)
    embeddings_df.to_csv('../data/embeddings.csv', index=False)

    print(f"Length of embedding vector: {len(embedding_table[0])}")

def go():
    load_dotenv()
    url = os.getenv('NEO4J_URI')
    username = os.getenv('NEO4J_USERNAME')
    password = os.getenv('NEO4J_PASSWORD')

    driver = init_driver(uri=url, username=username, password=password)

    try:
        create_skill_embeddings(driver)
    except Exception as e:
        print(f"An error occurred: {str(e)}")
    finally:
        close_driver(driver)

if __name__ == '__main__':
    go()
