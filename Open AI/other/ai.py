import os
import requests
import json

# Configuration
API_KEY = "e8f13f7e5ba348a5868176eabc1deff8"
headers = {
    "Content-Type": "application/json",
    "api-key": API_KEY,
}

ENDPOINT = "https://salespalcopilot.openai.azure.com/openai/deployments/gpt-4o/chat/completions?api-version=2024-02-15-preview"

# Initial system message (defining the assistant role)
system_message = {
    "role": "system",
    "content": "You are an AI assistant that helps people find information."
}

# Keep track of the conversation history
conversation_history = [system_message]

def send_message(user_input):
    # Add the user message to the conversation history
    conversation_history.append({"role": "user", "content": user_input})
    
    # Create payload with the updated conversation
    payload = {
        "messages": conversation_history,
        "temperature": 0.7,
        "top_p": 0.95,
        "max_tokens": 800
    }
    
    # Send request to the API
    try:
        response = requests.post(ENDPOINT, headers=headers, json=payload)
        response.raise_for_status()  # Will raise an HTTPError if the HTTP request returned an unsuccessful status code
        response_data = response.json()
        
        # Get the assistant's reply
        assistant_reply = response_data['choices'][0]['message']['content']
        
        # Add the assistant's reply to the conversation history
        conversation_history.append({"role": "assistant", "content": assistant_reply})
        
        return assistant_reply
    except requests.RequestException as e:
        raise SystemExit(f"Failed to make the request. Error: {e}")

# Interactive loop to ask questions
print("Ask your question (type 'exit' to stop):")

while True:
    user_input = input("> ")
    if user_input.lower() == 'exit':
        print("Goodbye!")
        break
    
    # Send the user question and get the assistant's response
    reply = send_message(user_input)
    
    # Print the assistant's response
    print(f"Assistant: {reply}")
