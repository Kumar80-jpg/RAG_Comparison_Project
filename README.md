# RAG vs Knowledge Graph vs Hybrid Graph

## 🔹 Traditional RAG
- Uses embeddings only
- No relationships
- Fast similarity search

## 🔹 Knowledge Graph
- Uses Neo4j
- Entities + relationships
- No semantic similarity

## 🔹 Hybrid Graph
- Combines both
- Graph + embeddings
- Foundation for GraphRAG

---

## ▶️ How to Run

### 1. Install
pip install -r requirements.txt

### 2. Run Neo4j

### 3. Run each module:

Traditional RAG:
python traditional_rag/main.py

Knowledge Graph:
python knowledge_graph/main.py

Hybrid Graph:
python hybrid_graph/main.py