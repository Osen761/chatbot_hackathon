import os
from dotenv import load_dotenv
from langchain_community.document_loaders import DirectoryLoader, TextLoader # Add PyPDFLoader if needed
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_community.vectorstores import Chroma

# --- Configuration ---
DATA_PATH = "sample_data/"
DB_PATH = "chroma_db"

def main():
    load_dotenv()
    api_key = os.getenv("GOOGLE_API_KEY")
    if not api_key:
        print("Error: GOOGLE_API_KEY not found in .env file.")
        return

    print("API Key loaded.")

    # --- Initialize Embeddings ---
    try:
        # Using the recommended model for text embedding
        embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001", google_api_key=api_key)
        print("Embeddings model loaded.")
    except Exception as e:
        print(f"Error loading embeddings model: {e}")
        return

    # --- Load Documents ---
    print(f"Loading documents from {DATA_PATH}...")
    try:
        # Using DirectoryLoader to load all .txt files
        loader = DirectoryLoader(DATA_PATH, glob="**/*.txt", loader_cls=TextLoader, show_progress=True)
        # Add other loaders here if needed (e.g., PyPDFLoader)
        documents = loader.load()
        if not documents:
            print("No documents found in the specified path.")
            return
        print(f"Loaded {len(documents)} documents.")
    except Exception as e:
        print(f"Error loading documents: {e}")
        return

    # --- Split Documents ---
    print("Splitting documents into chunks...")
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
    texts = text_splitter.split_documents(documents)
    print(f"Split into {len(texts)} chunks.")

    # --- Create and Persist Vector Store ---
    print(f"Creating vector store in {DB_PATH}...")
    try:
        vector_store = Chroma.from_documents(
            documents=texts,
            embedding=embeddings,
            persist_directory=DB_PATH
        )
        vector_store.persist() # Ensure data is saved
        print("Vector store created and persisted successfully!")
    except Exception as e:
        print(f"Error creating vector store: {e}")

if __name__ == "__main__":
    main()