from openai import OpenAI

command=1
client = OpenAI(
  api_key="<Your Key Here>",
)

completion = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "You are a person named {} who speaks hindi as well as english. He is from India and is a coder. You analyze chat history and respond like {}"},
    {"role": "user", "content": command}
  ]
)

print(completion.choices[0].message.content)