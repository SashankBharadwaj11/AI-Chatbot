from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Get required variables from environment
API_KEY = os.getenv("OPENAI_API_KEY")
ENDPOINT = os.getenv("AZURE_OPENAI_ENDPOINT")
DEPLOYMENT_ID = os.getenv("AZURE_OPENAI_DEPLOYMENT_ID")
API_VERSION = os.getenv("OPENAI_API_VERSION")

# Ensure all necessary environment variables are present
if not API_KEY or not ENDPOINT or not DEPLOYMENT_ID or not API_VERSION:
    raise ValueError("Missing required API credentials in the environment variables.")
