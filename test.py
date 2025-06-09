# Please install OpenAI SDK first: `pip3 install openai`

from openai import OpenAI


client = OpenAI(api_key="sk-9e216e3ec16e474f9a1e64f7ce848315", base_url="https://api.deepseek.com")

response = client.chat.completions.create(
    model="deepseek-chat",
    messages=[
        {"role": "system", "content": "You are a helpful assistant"},
        {"role": "user", "content": "Hello"},
    ],
    stream=False
)

print(response.choices[0].message.content)