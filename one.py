import openai
import os
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv('OPENAI_API_KEY')

response = openai.Completion.create(
    model = 'text-davinci-003',
    prompt = "Give me two reasons to learn OpenAPI with Python",
    max_tokens = 200
)

print(response['choices'][0]['text'])