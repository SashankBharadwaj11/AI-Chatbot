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
class SalesPalCopilot:
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
    def chat(self, transcription, speak_for_user=False):
        # Add user input (transcription) to memory
        self.memory.add_user_message(transcription)

        # Create the prompt for the model
        prompt = f"""
        You are an AI copilot assisting a salesperson in a live call. 
        The real-time transcription of the call is: "{transcription}".
        
        Based on this conversation, generate a helpful and persuasive response to assist the salesperson in progressing the sale.

        { 'The salesperson has asked you to speak on their behalf. Generate a response that can be spoken in their voice.' if speak_for_user else '' }

        Keep your responses professional, concise, and relevant to the conversation.
        """
        
        try:
            # Generate response from the LLM
            response = self.llm.invoke([HumanMessage(content=prompt)])  # Pass the prompt wrapped in a HumanMessage

            # Add assistant response to memory
            self.memory.add_ai_message(response.content)

            return response.content
        except Exception as e:
            # Catching and returning detailed error for debugging purposes
            return f"Error occurred during API call: {str(e)}"


# Create an instance of the SalesPalCopilot
copilot = SalesPalCopilot()

# Simulate interaction with the assistant
print("Enter the call transcription (type 'exit' to stop):")

while True:
    transcription = input("> ").strip()
    
    if transcription.lower() == 'exit':
        print("Goodbye!")
        break
    
    # Check if user wants the AI to speak on their behalf
    speak_for_user = input("Do you want the AI to speak for you? (yes/no): ").strip().lower() == 'yes'

    # Get the assistant's response
    reply = copilot.chat(transcription, speak_for_user)

    # Print the assistant's response
    print(f"Assistant: {reply}")
