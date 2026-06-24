def get_retriever(vectorstore, k=3):
    """
    Convert vectorstore into retriever
    """
    retriever = vectorstore.as_retriever(
        search_kwargs={"k": k}
    )
    return retriever