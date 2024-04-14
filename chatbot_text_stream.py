import openai
from dotenv import load_dotenv, find_dotenv

_ = load_dotenv(find_dotenv())

client = openai.Client()


def text_generate(messages, gpt_model, max_tokens=500, temperature=0):
    response = client.chat.completions.create(
        messages=messages,
        model=gpt_model,
        max_tokens=max_tokens,
        temperature=temperature,
        stream=True
    )

    complete_text = ''
    print('chatbot: ', end='')
    for stream_response in response:
        text = stream_response.choices[0].delta.content
        if text:
            print(text, end='')
            complete_text += text

    messages_list.append({'role': 'assistant', 'content': complete_text})


if __name__ == '__main__':
    messages_list = []
    model = 'gpt-4-turbo'
    print('chatbot: Hi! How can I help you today?')
    text_input = input('user: ')

    while text_input.lower() != 'thanks':
        if text_input.lower() == 'info':
            print(messages_list)
            text_input = input('\nuser: ')
        else:
            messages_list.append({'role': 'user', 'content': f'{text_input}'})
            text_generate(messages_list, model, 1000, 1)
            text_input = input('\nuser: ')
