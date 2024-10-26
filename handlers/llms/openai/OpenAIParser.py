from openai import AsyncClient


class OpenAIParser:
    def __init__(self) -> None:
        self.client = AsyncClient()
    
    
