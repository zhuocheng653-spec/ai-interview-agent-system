from rag.vector_store import VectorStore

store = VectorStore()

def load_knowledge():
    with open("rag/knowledge_base.txt", "r", encoding="utf-8") as f:
        lines = f.read().split("\n\n")
        for line in lines:
            store.add(line)

def retrieve(query):
    return store.search(query)
