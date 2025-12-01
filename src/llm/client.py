from openai import OpenAI
from pydantic import BaseModel
from settings.config import OPENAI_API_KEY

class LLMClient:
    def __init__(
        self
    ):
        api_key = OPENAI_API_KEY
        self.client = OpenAI(api_key=api_key)

    def generate_structured_response(self, 
        prompt: str,
        output_model: BaseModel,
        model: str = "gpt-4.1-mini",
        temperature: float = 0.0
    )-> BaseModel:
        response = self.client.responses.parse(
            model=model,
            input=prompt,
            temperature=temperature,
            text_format=output_model,
        )
        return response.output_parsed
    
    