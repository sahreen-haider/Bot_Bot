import os
import openai
import tiktoken
from dotenv import load_dotenv, find_dotenv

_ = load_dotenv(find_dotenv())


openai.api_key = os.environ['OPENAI_API_KEY']

client = openai.OpenAI()

def get_completions(prompt, model="gpt-3.5-turbo"):
    messages = [
        {"role": "system", "content": "you are a chatbot who talks like a pirate"},
        {"role": "user", "content": prompt}]
    response = client.chat.completions.create(
        model=model,
        messages=messages,
        temperature = 0
    )
    return response.choices[0].message.content

print(get_completions('what is a boat ?'))


