import google.generativeai as genai
import os
from dotenv import load_dotenv

def main():
    # Load environment variables from .env file
    load_dotenv()

    # Fetch the API key
    api_key = os.getenv("GOOGLE_API_KEY")
    if not api_key:
        print("Error: GOOGLE_API_KEY not found.")
        print("Please create a .env file with your API key (see .env.example).")
        return

    # Configure the generative AI library
    try:
        genai.configure(api_key=api_key)
        model = genai.GenerativeModel('gemini-pro')
        print("Gemini model loaded successfully.")
        print("Starting chat... Type 'quit', 'exit', or 'bye' to end.")
    except Exception as e:
        print(f"Error configuring Gemini or loading model: {e}")
        return

    # Start the chat loop
    while True:
        try:
            user_input = input("You: ")
            if user_input.lower() in ['quit', 'exit', 'bye']:
                print("Chat ended.")
                break

            if not user_input:
                continue

            # Send message to Gemini and get response
            response = model.generate_content(user_input)

            # Print the response text
            print(f"Gemini: {response.text}")

        except Exception as e:
            print(f"An error occurred: {e}")
        except KeyboardInterrupt:
            print("\nChat interrupted by user. Exiting.")
            break

if __name__ == "__main__":
    main()