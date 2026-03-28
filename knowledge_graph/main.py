from entity_extractor import extract_entities
from neo4j_connection import Neo4jConnection

text = """
Google uses AI in healthcare.
Microsoft uses AI in finance.
"""

db = Neo4jConnection()
entities = extract_entities(text)

print("Entities:", entities)  # debug

# Create nodes
for entity, label in entities:
    db.run("MERGE (n:Entity {name: $name})", {"name": entity})

# Create relationships
for i in range(len(entities)-1):
    db.run("""
    MATCH (a:Entity {name:$a}), (b:Entity {name:$b})
    MERGE (a)-[:RELATED_TO]->(b)
    """, {"a": entities[i][0], "b": entities[i+1][0]})

db.close()