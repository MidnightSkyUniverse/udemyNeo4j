"""
    Test query Neo4j schema
"""
from langchain.chains import GraphCypherQAChain
from langchain_community.graphs import Neo4jGraph
from langchain_openai import ChatOpenAI
from langchain.prompts.prompt import PromptTemplate

from dotenv import load_dotenv
import os


def go():
    load_dotenv()
    try:
        graph = Neo4jGraph(
            url=os.getenv("NEO4J_URI"),
            username=os.getenv("NEO4J_USERNAME"),
            password=os.getenv("NEO4J_PASSWORD")
        )

        # print(graph.schema)

        CYPHER_GENERATION_TEMPLATE = """Task:Generate Cypher statement to query a graph database.
           Instructions:
           Use only the provided relationship types and properties in the schema.
           Do not use any other relationship types or properties that are not provided.
           Schema:
           {schema}
           Note: 
           Do not include any text except the generated Cypher statement.
           Do not return embedding property from Skill node.
           Examples: Here are a few examples of generated Cypher statements for particular questions:
           # What skills mention Oracle?
           MATCH (s:Skill) WHERE s.name CONTAINS 'Oracle' RETURN s.name, s.description

           The question is:
           {question}"""

    except Exception as e:
        print(f"An error occurred: {str(e)}")



if __name__=='__main__':
    go()