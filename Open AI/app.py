from assistant import LangChainAssistant

if __name__ == "__main__":
    assistant = LangChainAssistant()
    
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
