import re

from ollama import chat
from ollama import ChatResponse

# MODEL = 'llama3.2'
MODEL = 'deepseek-r1'
# MODEL = 'gemma3:4b'

CONTEXT = """You are an AI assistant that generates varying fun facts.
            Answer with a random fun fact. Start the sentence with "Did you know..." or something similar.
            Don't use more then 3 sentences. Keep each sentence short and not longer than 7 words.
            Do not include any other information. 
            Do not include any disclaimers.
            Do not include any explanations.
            Do not include any additional information.
            Do not include any examples.
            Do not include any sources.
            Do not include any links.
            Do not include any URLs.
            """


class FunFactGenerator:

    @staticmethod
    async def __query_llm(messages: [str]) -> ChatResponse:
        response: ChatResponse = chat(model=MODEL, messages=messages)
        return response

    async def llm(self) -> str:
        response: ChatResponse = await self.__query_llm([
            {"role": "system", "content": CONTEXT},
            {
                'role': 'user',
                'content': f'Generate me an interesting fun fact, please.',
            },
        ])
        response_msg = response["message"]["content"]
        if MODEL == 'deepseek-r1':
            response_msg = re.sub(r'<think>.*?</think>', '', response_msg, flags=re.DOTALL)
        return response_msg

    async def llm_categories(self, category: str) -> str:
        response: ChatResponse = await self.__query_llm([
            {"role": "system", "content": CONTEXT},
            {
                'role': 'user',
                'content': f'Generate me an interesting fun fact about the category {category}, please.',
            },
        ])
        response_msg = response["message"]["content"]
        if MODEL == 'deepseek-r1':
            response_msg = re.sub(r'<think>.*?</think>', '', response_msg, flags=re.DOTALL)
        return response_msg
