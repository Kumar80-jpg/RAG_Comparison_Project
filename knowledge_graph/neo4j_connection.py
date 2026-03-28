from neo4j import GraphDatabase

class Neo4jConnection:
    def __init__(self):
        self.driver = GraphDatabase.driver(
            "bolt://127.0.0.1:7687",
            auth=("neo4j", "12345678")
        )

    def run(self, query, params=None):
        with self.driver.session() as session:
            session.run(query, params)

    def close(self):   # ✅ ADD THIS
        self.driver.close()