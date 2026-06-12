# Mini-RAG-Chatbot
# Mini RAG Chatbot

## Overview

This project is a simple implementation of a Retrieval-Augmented Generation (RAG) chatbot built using Streamlit, LangChain, ChromaDB, and Sentence Transformers.

The chatbot retrieves relevant information from a knowledge base using vector similarity search and displays context-based responses to user queries.

---

## Features

* Interactive Streamlit interface
* Document chunking using LangChain
* Text embeddings using Sentence Transformers
* Vector storage with ChromaDB
* Similarity search for information retrieval
* Basic RAG workflow implementation

---

## Technologies Used

* Python
* Streamlit
* LangChain
* ChromaDB
* Sentence Transformers
* HuggingFace Embeddings

---

## RAG Workflow

1. Load the document or knowledge base.
2. Split the content into smaller chunks.
3. Generate embeddings for each chunk.
4. Store embeddings in ChromaDB.
5. Convert the user query into an embedding.
6. Perform similarity search to retrieve relevant chunks.
7. Display the retrieved information to the user.

---

## Project Structure

Mini-RAG-Chatbot/

├── app.py

├── README.md

└── requirements.txt

---

## How to Run

1. Install dependencies:

pip install -r requirements.txt

2. Run the application:

python -m streamlit run app.py

3. Open the local Streamlit URL displayed in the terminal.

---

## Future Improvements

* PDF document upload support
* Integration with Large Language Models (LLMs)
* Chat history and memory
* Multi-document support
* Improved response generation

---

## Author

Vanshita Sinha
