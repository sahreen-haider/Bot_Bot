import os
import openai
import tiktoken
from dotenv import load_dotenv, find_dotenv
from system_message import *

_ = load_dotenv(find_dotenv())


openai.api_key = os.environ['OPENAI_API_KEY']

client = openai.OpenAI()

def get_completions(prompt, model="gpt-3.5-turbo", temperature=0.6, max_tokens=300):
    messages = [
        {"role": "system", "content": system_messages},
        {"role": "user", "content": f"{delimiter}{prompt}{delimiter}"}]
    response = client.chat.completions.create(
        model=model,
        messages=messages,
        temperature = temperature,
        max_tokens=max_tokens
    )
    return response.choices[0].message.content





try:
    final_res = get_completions(f"""
    by how much is the BlueWave Chromebook more expensive \
    than the TechPro Desktop""", temperature=0.9, max_tokens=1000)
    final_res = final_res.split(delimiter)[-1].strip()

except:
    final_res = "Sorry, There is an issue right now, Please try again later"

print(final_res)