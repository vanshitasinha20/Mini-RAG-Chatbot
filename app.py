import streamlit as st

from langchain_core.documents import Document
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma

st.title("Mini RAG Chatbot")

documents = [
    Document(
        page_content="""
        RAG stands for Retrieval Augmented Generation.

        ChromaDB is a vector database used to store embeddings.

        Embeddings convert text into numerical vectors.

        LangChain is a framework used to build LLM applications.

        Vector databases help retrieve relevant information using similarity search.
        """
    )
]

splitter = RecursiveCharacterTextSplitter(
    chunk_size=100,
    chunk_overlap=20
)

docs = splitter.split_documents(documents)

embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

db = Chroma.from_documents(
    docs,
    embeddings
)

question = st.text_input("Ask a Question")

if question:

    results = db.similarity_search(
        question,
        k=2
    )

    st.subheader("Retrieved Information")

    for doc in results:
        st.write(doc.page_content)