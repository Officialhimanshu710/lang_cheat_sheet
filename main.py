import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq

# Load environment variables from .env file
load_dotenv()

# Initialize ChatGroq model
llm = ChatGroq(
    model="openai/gpt-oss-120b",
)

def main():
    response = llm.invoke("Hello, introduce yourself briefly.")
    print("Response from Groq:")
    print(response.content)

if __name__ == "__main__":
    main()