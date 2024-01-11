"""
    Create graph database
"""
import os
from dotenv import load_dotenv
import json
from utils import (
    init_driver,
    close_driver,
    execute_query,
    clean_up_database,
)


CSV_WITH_TITLES_URL = 'https://raw.githubusercontent.com/MidnightSkyUniverse/udemyNeo4j/master/data/titles_and_skills.csv'
CSV_WITH_SKILLS_URL = 'https://raw.githubusercontent.com/MidnightSkyUniverse/udemyNeo4j/master/data/skills_details.csv'


CREATE_CONSTRAINTS_QUERIES = [
        """CREATE CONSTRAINT skillUnique IF NOT EXISTS FOR (s:Skill) REQUIRE s.name IS UNIQUE
        """,
        """CREATE CONSTRAINT titleUnique IF NOT EXISTS FOR (t:Title) REQUIRE t.name IS UNIQUE
        """,
        """SHOW ALL CONSTRAINTS""",
    ]

CREATE_DATA_MODEL_QUERIES = [
        f"""LOAD CSV WITH HEADERS FROM '{CSV_WITH_TITLES_URL}' AS row 
            MERGE (t:Title {{name: row.Title}})
        """,
        f"""LOAD CSV WITH HEADERS from '{CSV_WITH_SKILLS_URL}' AS row 
            MERGE (s:Skill {{name: row.Skill}}) 
            SET s.id = row.ID, 
                s.description = row.Description, 
                s.category=row.Category
        """,
        f"""LOAD CSV WITH HEADERS from '{CSV_WITH_TITLES_URL}' AS row 
            MATCH (t:Title {{name: row.Title}}) 
            SET t.skills = split(row.Skills, '|')
        """,
        """MATCH (t:Title) 
            UNWIND t.skills AS skill 
            MERGE (s:Skill {name: skill}) 
            MERGE (t)-[:REQUIRES]->(s)
        """,
        """MATCH (t:Title) REMOVE t.skills
        """,
        """MATCH (s:Skill{category:'Certification'}) 
            SET s:Skill:Certification 
        """,
        """MATCH (s:Skill{category:'SpecializedSkill'}) 
            SET s:Skill:SpecializedSkill 
        """,
        """MATCH (s:Skill) REMOVE s.category
        """,
         """MATCH (t:Title)-[r:REQUIRES]-(s:Skill)
            RETURN COUNT(DISTINCT t) AS TotalTitles, COUNT(r) AS TotalRequires, COUNT(DISTINCT s) AS TotalSkills
        """,
    ]


def go():
    pass




if __name__ == '__main__':
    go()