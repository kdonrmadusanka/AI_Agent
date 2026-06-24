from langchain_community.vectorstores import FAISS


def create_vectorstore(chunks, embeddings):
    """
    Create FAISS vector DB from chunks
    """
    db = FAISS.from_documents(chunks, embeddings)
    return db


def save_vectorstore(db, path="faiss_index"):
    """
    Save FAISS index locally
    """
    db.save_local(path)


def load_vectorstore(path, embeddings):
    """
    Load FAISS index from disk
    """
    db = FAISS.load_local(
        path,
        embeddings,
        allow_dangerous_deserialization=True
    )
    return db