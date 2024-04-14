import openai
from dotenv import load_dotenv, find_dotenv

_ = load_dotenv(find_dotenv())

client = openai.Client()

messages_list = []
model = 'gpt-3.5-turbo-0125'


def text_generate(messages, gpt_model, max_tokens=1000, temperature=0):
    response = client.chat.completions.create(
        messages=messages,
        model=gpt_model,
        max_tokens=max_tokens,
        temperature=temperature
    )
    messages_list.append(response.choices[0].message.model_dump(exclude_none=True))

    print(f'ChatGPT: {messages[-1]["content"]}')
    print(f'Tokens: {response.usage.total_tokens}')


text = input('Make a question: ')

while text.lower() != 'thanks':
    if text.lower() == 'info':
        print(messages_list)
        text = input('Question: ')
    else:
        messages_list.append({'role': 'user', 'content': f'{text}'})
        text_generate(messages_list, model, 1000, 0.8)
        text = input('Question: ')
