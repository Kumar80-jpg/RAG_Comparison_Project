from neo4j import GraphDatabase

driver = GraphDatabase.driver(
    "neo4j://127.0.0.1:7687",
    auth=("neo4j", "12345678")
)

try:
    with driver.session() as session:
        result = session.run("RETURN 'Connected Successfully' AS msg")
        print(result.single()["msg"])
except Exception as e:
    print("ERROR:", e)