from langchain_openai import AzureChatOpenAI
from langchain.memory import ChatMessageHistory  # or use langchain_community if needed
from langchain.schema import HumanMessage
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Get the OpenAI API key, Azure endpoint, deployment name, and API version from environment variables
API_KEY = os.getenv("OPENAI_API_KEY")
ENDPOINT = os.getenv("AZURE_OPENAI_ENDPOINT")
DEPLOYMENT_ID = os.getenv("AZURE_OPENAI_DEPLOYMENT_ID")
API_VERSION = os.getenv("OPENAI_API_VERSION")

# Check if all environment variables are properly loaded
if not API_KEY or not ENDPOINT or not DEPLOYMENT_ID or not API_VERSION:
    raise ValueError("Missing required API credentials in the environment variables.")

# Define the LLM using Azure OpenAI
class LangChainAssistant:
    def __init__(self):
        # Initialize Azure OpenAI Chat model
        self.llm = AzureChatOpenAI(
            openai_api_key=API_KEY,
            azure_endpoint=ENDPOINT,
            deployment_name=DEPLOYMENT_ID,
            api_version=API_VERSION
        )
        # Set up memory for conversation
        self.memory = ChatMessageHistory()

    # Method to interact with the assistant
    def chat(self, query):
        # Add user input to memory
        self.memory.add_user_message(query)

        try:
            # Generate response from the LLM
            response = self.llm.invoke([HumanMessage(content=query)])  # Pass the query wrapped in a HumanMessage

            # Add assistant response to memory
            self.memory.add_ai_message(response.content)
            return response.content
        except Exception as e:
            # Catching and returning detailed error for debugging purposes
            return f"Error occurred during API call: {str(e)}"


# Create an instance of the assistant
assistant = LangChainAssistant()

# Start an interactive loop to ask questions
print("Ask your question (type 'exit' to stop):")

while True:
    user_input = input("> ").strip()
    if user_input.lower() == 'exit':
        print("Goodbye!")
        break

    # Get the assistant's response
    reply = assistant.chat(user_input)

    # Print the assistant's response
    print(f"Assistant: {reply}")
