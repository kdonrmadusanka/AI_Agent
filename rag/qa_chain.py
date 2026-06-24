from langchain_openai import ChatOpenAI
from config import OPENAI_API_KEY


def get_llm():
    """
    Initialize LLM (GPT model)
    """
    llm = ChatOpenAI(
        api_key=OPENAI_API_KEY,
        model="gpt-4.1-mini",
        temperature=0.2
    )
    return llm


def format_docs(docs):
    """
    Convert retrieved documents into single context string
    """
    return "\n\n".join([doc.page_content for doc in docs])


def answer_question(llm, retriever, question: str):
    """
    RAG pipeline:
    1. Retrieve relevant chunks
    2. Format context
    3. Send to LLM
    4. Return answer
    """

    # Step 1: Retrieve
    docs = retriever.invoke(question)

    # Step 2: Format context
    context = format_docs(docs)

    # Step 3: Prompt
    prompt = f"""
You are a helpful assistant. Answer ONLY using the context below.

Context:
{context}

Question:
{question}

If the answer is not in the context, say "I don't know based on the document."
"""

    # Step 4: Get response
    response = llm.invoke(prompt)

    return response.content