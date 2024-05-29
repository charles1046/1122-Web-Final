from configparser import ConfigParser
from langchain_google_genai import ChatGoogleGenerativeAI
import os


class LLM:
    def __init__(self):
        self.config = ConfigParser()
        self.config.read("config.ini")
        self.llm = ChatGoogleGenerativeAI(
            model=os.environ.get('model'),
            google_api_key=os.environ.get('API_KEY')
        )

    def invoke(self, text: str):
        result = self.llm.invoke(text)
        return result
