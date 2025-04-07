# RAG Chatbot Starter (Gemini + Langchain + ChromaDB)

This template provides a command-line chatbot implementing the Retrieval-Augmented Generation (RAG) pattern. It uses Langchain to orchestrate Google Gemini, ChromaDB (as a vector store), and your custom data.

## Setup

1.  **API Key:**
    * Rename the `.env.example` file in this directory to `.env`.
    * Open the `.env` file and paste your Google Gemini API key in place of `"YOUR_API_KEY_HERE"`.

2.  **Install Dependencies:**
    * Open your terminal in this directory (`rag-chatbot`).
    * Install the required Python libraries:
        ```bash
        pip install -r requirements.txt
        ```
    * *(Optional: If you want to process PDFs, uncomment `pypdf` in `requirements.txt` and reinstall)*

3.  **Prepare Data:**
    * Place the text files (.txt), PDFs (.pdf), or other documents you want the chatbot to know about inside the `sample_data/` folder. A `sample.txt` file is included as an example.

## Running the Chatbot (2 Steps)

**Step 1: Ingest Data into Vector Store**

* Run the `ingest.py` script first. This reads documents from `sample_data/`, splits them, creates embeddings (using Gemini), and stores them in a local ChromaDB database (in a folder named `chroma_db`).
    ```bash
    python ingest.py
    ```
* You only need to run this again if you add or change files in `sample_data/`.

**Step 2: Run the RAG Chatbot**

* Execute the `main.py` script:
    ```bash
    python main.py
    ```
* The script will load the Gemini model and connect to the ChromaDB database you created.
* It will prompt you with `Ask question about your documents: `. Type your question related to the content in `sample_data/` and press Enter.
* The chatbot will retrieve relevant information and use Gemini to generate an answer.
* Type `quit`, `exit`, or `bye` to end the chat session.

## How it Works

* **`ingest.py`**: Loads documents, splits them into chunks, generates vector embeddings using a Gemini embedding model, and stores them in ChromaDB.
* **`main.py`**:
    * Loads the Gemini chat model and embedding model.
    * Connects to the existing ChromaDB database.
    * Sets up a Langchain `RetrievalQA` chain.
    * When you ask a question:
        1.  The retriever searches ChromaDB for relevant document chunks.
        2.  The relevant chunks and your question are put into a prompt.
        3.  The prompt is sent to Gemini via Langchain.
        4.  The generated answer is printed.