import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI, GoogleGenerativeAIEmbeddings
from langchain_community.vectorstores import Chroma
from langchain.prompts import PromptTemplate
from langchain.chains import RetrievalQA

# --- Configuration ---
DB_PATH = "chroma_db"
PROMPT_TEMPLATE = """Answer the question based only on the following context:

{context}

---
Answer the question based on the context above: {question}
"""

def main():
    load_dotenv()
    api_key = os.getenv("GOOGLE_API_KEY")
    if not api_key:
        print("Error: GOOGLE_API_KEY not found in .env file.")
        return

    print("API Key loaded.")

    # --- Initialize LLM and Embeddings ---
    try:
        llm = ChatGoogleGenerativeAI(model="gemini-pro", google_api_key=api_key,
                                     temperature=0.3, convert_system_message_to_human=True)
        embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001", google_api_key=api_key)
        print("LLM and Embeddings models loaded.")
    except Exception as e:
        print(f"Error loading Google models: {e}")
        return

    # --- Load Vector Store ---
    if not os.path.exists(DB_PATH):
         print(f"Error: Chroma database not found at {DB_PATH}.")
         print("Please run ingest.py first to create the database.")
         return

    print(f"Loading vector store from {DB_PATH}...")
    try:
        vector_store = Chroma(persist_directory=DB_PATH, embedding_function=embeddings)
        retriever = vector_store.as_retriever()
        print("Vector store loaded successfully.")
    except Exception as e:
        print(f"Error loading vector store: {e}")
        return

    # --- Create RAG Chain ---
    prompt = PromptTemplate(template=PROMPT_TEMPLATE, input_variables=["context", "question"])
    qa_chain = RetrievalQA.from_chain_type(
        llm=llm,
        chain_type="stuff",  # Options: "stuff", "map_reduce", "refine", "map_rerank"
        retriever=retriever,
        return_source_documents=False, # Set to True if you want to see source chunks
        chain_type_kwargs={"prompt": prompt}
    )
    print("RAG chain created.")

    # --- Start Chat Loop ---
    print("\nChatbot ready! Ask questions about your documents.")
    print("Type 'quit', 'exit', or 'bye' to end.")

    while True:
        try:
            user_input = input("\nAsk question about your documents: ")
            if user_input.lower() in ['quit', 'exit', 'bye']:
                print("Chat ended.")
                break
            if not user_input.strip():
                continue

            # --- Get Answer from RAG Chain ---
            print("Thinking...")
            result = qa_chain.invoke({"query": user_input})

            print("\nAnswer:")
            print(result["result"])

            # Optional: Print source documents if needed
            # if result.get("source_documents"):
            #     print("\nSources:")
            #     for doc in result["source_documents"]:
            #         print(f"- {doc.metadata.get('source', 'Unknown')}")


        except Exception as e:
            print(f"An error occurred: {e}")
        except KeyboardInterrupt:
            print("\nChat interrupted by user. Exiting.")
            break

if __name__ == "__main__":
    main()