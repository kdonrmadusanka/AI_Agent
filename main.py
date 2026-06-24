from rag.loader import load_pdf
from rag.chunking import split_documents
from rag.embeddings import get_embeddings
from rag.vectorstore import create_vectorstore, save_vectorstore
from rag.retriever import get_retriever
from rag.qa_chain import get_llm, answer_question

# 1. Load PDF
docs = load_pdf("data/intro.pdf")

# 2. Split into chunks
chunks = split_documents(docs)

# 3. Create embeddings
embeddings = get_embeddings()

# 4. Create vector database
db = create_vectorstore(chunks, embeddings)

# Optional: save index
save_vectorstore(db)

# 5. Create retriever
retriever = get_retriever(db)

# 6. Load LLM
llm = get_llm()

# 7. Chat loop (interactive)
print("\n📄 PDF RAG Agent Ready! Ask questions...\n")

while True:
    question = input("You: ")

    if question.lower() in ["exit", "quit"]:
        break

    answer = answer_question(llm, retriever, question)


    print("\nAI:", answer, "\n")