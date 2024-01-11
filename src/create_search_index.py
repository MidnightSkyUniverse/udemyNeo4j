"""
Create search index for skills in the Udemy training project
"""

import os
from dotenv import load_dotenv
import json
from utils import (
    init_driver,
    close_driver,
    execute_query,
)

# Constants
CSV_EMBEDDINGS_URL = 'https://raw.githubusercontent.com/MidnightSkyUniverse/udemyNeo4j/master/data/embeddings.csv'

INSERT_EMBEDDINGS_QUERY = f"""
    LOAD CSV WITH HEADERS FROM '{CSV_EMBEDDINGS_URL}' AS row
    MATCH (s:Skill {{name: row.Skill}})
    CALL db.create.setNodeVectorProperty(s, 'embedding', apoc.convert.fromJsonList(row.Embedding))
    RETURN count(*) as embeddingsAdded
"""

CREATE_INDEX_QUERY = """
    CALL db.index.vector.createNodeIndex(
    'skillDescription',
    'Skill',
    'embedding',
    384,
    'cosine'
)
"""

CHECK_INDEX_QUERY = """SHOW INDEXES YIELD id, name, type WHERE type='VECTOR' """

def go():
    pass



if __name__ == '__main__':
    go()