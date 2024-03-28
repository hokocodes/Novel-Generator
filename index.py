from openai import OpenAI
import os

client = OpenAI()
OpenAI.api_key = os.getenv('OPENAI_API_KEY')
completion = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "plotter", "content": "You are a plot creater, craft a new and unique plot for a book."},
  ]
)

print(completion.choices[0].message)