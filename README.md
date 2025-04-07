# Hackathon Starter Pack: Gemini Chatbots

This repository provides two basic Python starter templates for building chatbots using Google's Gemini API during the hackathon.

## Templates Included:

1.  **`simple-gemini-chat/`**:
    * A very basic command-line chat application that directly interacts with the Gemini API.
    * Useful for understanding direct LLM interaction.

2.  **`rag-chatbot/`**:
    * A more advanced command-line chatbot implementing the Retrieval-Augmented Generation (RAG) pattern.
    * Uses Langchain to orchestrate interactions between Gemini, a ChromaDB vector database (for custom knowledge), and the user.
    * Allows the chatbot to answer questions based on documents you provide in the `sample_data` folder.

## Getting Started

1.  **Clone or Fork:** Clone or fork this repository to your local machine or GitHub account.
2.  **Choose a Template:** Navigate into either the `simple-gemini-chat` or `rag-chatbot` directory based on your needs.
3.  **Follow Instructions:** Follow the specific `README.md` file within the chosen template directory for setup and execution instructions.

**Prerequisites:**

* Python 3.8+ installed.
* Access to the internet.
* A Google Gemini API Key (you can get one from [Google AI Studio](https://ai.google.dev/)).

Good luck with the hackathon!