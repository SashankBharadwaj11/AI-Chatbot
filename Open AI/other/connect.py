from langchain_openai import AzureChatOpenAI

# Basic test with LangChain OpenAI integration
def simple_langchain_test():
    try:
        llm = AzureChatOpenAI(
            openai_api_key="e8f13f7e5ba348a5868176eabc1deff8",
            azure_endpoint="https://salespalcopilot.openai.azure.com/",
            deployment_name="gpt-4o",
            api_version="2024-02-15-preview"
        )
        response = llm.invoke([{"role": "user", "content": "Explain what LangChain is."}])
        print(response.content)
    except Exception as e:
        print(f"Error: {str(e)}")

simple_langchain_test()

