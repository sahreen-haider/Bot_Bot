import os
import openai
import tiktoken
from dotenv import load_dotenv, find_dotenv

_ = load_dotenv(find_dotenv())


openai.api_key = os.environ['OPENAI_API_KEY']

client = openai.OpenAI()

def get_completions(prompt, model="gpt-3.5-turbo", temperature=0.6, max_tokens=300):
    messages = [
        {"role": "system", "content": "you are a chatbot who talks like a pirate and answers everything with more than 1000 words"},
        {"role": "user", "content": prompt}]
    response = client.chat.completions.create(
        model=model,
        messages=messages,
        temperature = temperature,
        max_tokens=max_tokens
    )
    return response.choices[0].message.content

print(get_completions('write a poem about sea ?', temperature=0.9, max_tokens=1000))

