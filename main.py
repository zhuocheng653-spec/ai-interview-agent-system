from demo.cli_demo import run_demo
from rag.retriever import load_knowledge

if __name__ == "__main__":
    load_knowledge()
    run_demo()
