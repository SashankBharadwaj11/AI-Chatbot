from langchain_openai import AzureChatOpenAI
from langchain.schema import HumanMessage
from memory import MemoryHandler
from langchain_community.chat_message_histories import ChatMessageHistory  # Updated import
from config import API_KEY, ENDPOINT, DEPLOYMENT_ID, API_VERSION

class LangChainAssistant:
    def __init__(self):
        # Initialize Azure OpenAI Chat model
        self.llm = AzureChatOpenAI(
            openai_api_key=API_KEY,
            azure_endpoint=ENDPOINT,
            deployment_name=DEPLOYMENT_ID,
            api_version=API_VERSION
        )
        # Initialize conversation memory with ChatMessageHistory
        self.memory = MemoryHandler(ChatMessageHistory())

        # Define the prompt for the SalesPal Copilot
        self.prompt = (
            "You are the SalesPal Copilot, an AI assistant designed to assist sales representatives during their calls. "
            "Your primary goal is to help the user effectively engage with customers by providing relevant information "
        )

    def chat(self, query):
        # Add user input to memory
        self.memory.add_user_message(query)

        try:
            # Create a full prompt by combining the predefined prompt with the user input
            full_prompt = f"{self.prompt}\nUser Input: {query}\nExpected AI Output:"
            
            # Generate response from the LLM using the full prompt
            response = self.llm.invoke([HumanMessage(content=full_prompt)])

            # Add assistant response to memory
            self.memory.add_ai_message(response.content)
            return response.content
        except Exception as e:
            return f"Error occurred during API call: {str(e)}"
