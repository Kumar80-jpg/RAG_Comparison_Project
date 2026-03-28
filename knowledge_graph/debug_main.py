# debug_main.py

from neo4j import GraphDatabase

driver = GraphDatabase.driver(
    "neo4j+s://706fbc53.databases.neo4j.io",
    auth=("neo4j", "1vnLLuydtvkdhz3LB-UnKJqc5eb0FERIJVJKpMLPiBM")
)

with driver.session() as session:
    session.run("CREATE (n:Test {name:'Hello'})")

print("Inserted successfully")