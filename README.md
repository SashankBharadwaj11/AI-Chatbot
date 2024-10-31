# AI Chatbot using Langchain and Azure OpenAI

## Overview

This repository contains an AI chatbot developed using Langchain and Azure OpenAI. The chatbot is designed to provide interactive and intelligent responses to user queries, utilizing the capabilities of OpenAI's language models for enhanced conversational experiences.

## Features

- **Natural Language Processing**: Understands and responds to user queries in natural language.
- **Contextual Awareness**: Maintains conversation context for more relevant responses.
- **Customizable**: Easily extend the functionality to suit various use cases.
- **Integration with Azure OpenAI**: Leverages Azure's powerful AI infrastructure for robust performance.

## Technologies Used

- **Langchain**: A framework for building applications powered by language models.
- **Azure OpenAI Service**: Provides access to OpenAI's models through Azure.
- **Python**: The programming language used for development.

## Getting Started

### Prerequisites

- Python 3.7 or higher
- Azure account with OpenAI Service access
- Required Python packages Langchain, Azureopen ai

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/your-repo-name.git
   cd your-repo-name
   
2. Create a virtual environment (optional but recommended):
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   
3. Install the required packages:
   pip install -r requirements.txt

4. Set up Azure OpenAI configuration:
   Create a .env file in the root directory and add your Azure OpenAI credentials:
   AZURE_OPENAI_API_KEY=your_api_key
   AZURE_OPENAI_ENDPOINT=https://your-openai-endpoint.azure.com/

### Usage

- Type your queries in the input box and hit Enter to receive responses from the chatbot.
- You can ask questions, seek information, or engage in casual conversation.
