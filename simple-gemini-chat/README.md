# Simple Gemini Chat Starter

This template provides a basic command-line interface to chat directly with the Google Gemini API.

## Setup

1.  **API Key:**
    * Rename the `.env.example` file in this directory to `.env`.
    * Open the `.env` file and paste your Google Gemini API key in place of `"YOUR_API_KEY_HERE"`.

2.  **Install Dependencies:**
    * Open your terminal in this directory (`simple-gemini-chat`).
    * Install the required Python libraries:
        ```bash
        pip install -r requirements.txt
        ```

## Running the Chatbot

1.  Execute the main script from your terminal:
    ```bash
    python main.py
    ```
2.  The script will prompt you with `You: `. Type your message and press Enter.
3.  The chatbot's response (from Gemini) will be printed.
4.  Type `quit`, `exit`, or `bye` to end the chat session.

## How it Works

This script uses the `google-generativeai` library to:
1.  Load your API key.
2.  Initialize the Gemini Pro model.
3.  Enter a loop that takes your input, sends it to the Gemini API, and prints the response.