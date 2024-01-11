//LOAD CSV WITH HEADERS from 'file:///titles_and_skills.csv'
//AS row  RETURN row.Title, row.Skill LIMIT 15;
////
//LOAD CSV WITH HEADERS from 'file:///skills_details.csv'
//AS row  RETURN row.ID, row.Skill, row.Description, row.Category LIMIT 15;

MATCH (n)  DETACH DELETE n;

DROP CONSTRAINT skillUnique IF EXISTS;
DROP CONSTRAINT titleUnique IF EXISTS;

DROP INDEX skillDescription IF EXISTS;

//// Create Constraints
CREATE CONSTRAINT skillUnique IF NOT EXISTS FOR (s:Skill) REQUIRE s.name IS UNIQUE;

CREATE CONSTRAINT titleUnique IF NOT EXISTS FOR (t:Title) REQUIRE t.name IS UNIQUE;

SHOW ALL CONSTRAINTS;


//// Import data
LOAD CSV WITH HEADERS from 'https://raw.githubusercontent.com/MidnightSkyUniverse/udemyNeo4j/master/data/titles_and_skills.csv' AS row MERGE (t:Title {name: row.Title});

LOAD CSV WITH HEADERS from 'https://raw.githubusercontent.com/MidnightSkyUniverse/udemyNeo4j/master/data/skills_details.csv' AS row MERGE (s:Skill {name: row.Skill}) SET s.id = row.ID, s.description = row.Description, s.category=row.Category;

LOAD CSV WITH HEADERS from 'https://raw.githubusercontent.com/MidnightSkyUniverse/udemyNeo4j/master/data/titles_and_skills.csv' AS row MATCH (t:Title {name: row.Title}) SET t.skills = split(row.Skills, '|');


MATCH (t:Title) UNWIND t.skills AS skill MERGE (s:Skill {name: skill}) MERGE (t)-[:REQUIRES]->(s);

MATCH (t:Title) REMOVE t.skills;

//MATCH (s:Skill) RETURN DISTINCT s.category;

//// Set another label for node Skill
MATCH (s:Skill{category:'Certification'}) SET s:Skill:Certification return s.name, labels(s);

MATCH (s:Skill{category:'SpecializedSkill'}) SET s:Skill:SpecializedSkill return s.name, labels(s);

MATCH (s:Skill) REMOVE s.category;

//MATCH (t:Title)-[r:REQUIRES]-(s:Skill) RETURN t,r,s;


