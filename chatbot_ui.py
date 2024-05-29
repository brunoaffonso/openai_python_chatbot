import streamlit as st
import openai


def text_generate(messages,
                  openai_key,
                  model='gpt-4o',
                  temperature=0,
                  stream=False):
    openai.api_key = openai_key
    response = openai.chat.completions.create(
        messages=messages,
        model=model,
        temperature=temperature,
        stream=stream
    )
    return response


def main_page():
    st.set_page_config(
        layout="wide",
        page_title="Chatbot",
        page_icon="🤖",
        initial_sidebar_state="expanded",
    )

    api_key = st.sidebar.text_input('OpenAI API Key', type='password')

    button = st.sidebar.button('Clear Chat')
    if button:
        st.session_state['messages'] = []

    if not 'messages' in st.session_state:
        st.session_state['messages'] = []

    messages = st.session_state['messages']

    st.header('🤖 Chatbot', divider=True)

    for message in messages:
        chat = st.chat_message(message['role'])
        chat.markdown(message['content'])

    if api_key:
        prompt = st.chat_input('Faça uma pergunta...')
        if prompt:
            new_message = {'role': 'user', 'content': prompt}
            chat = st.chat_message(new_message['role'])
            chat.markdown(new_message['content'])
            messages.append(new_message)

            chat = st.chat_message('assistant')
            placeholder = chat.empty()
            placeholder.markdown('▌')
            full_response = ''
            responses = text_generate(messages,
                                      api_key,
                                      stream=True)
            for response in responses:
                response_fragment = response.choices[0].delta.content if response.choices[0].delta.content else ''
                full_response += response_fragment
                placeholder.markdown(full_response + "▌")
            placeholder.markdown(full_response)
            new_message = {'role': 'assistant',
                           'content': full_response}
            messages.append(new_message)

            st.session_state['messages'] = messages
    else:
        st.info('Please enter your OpenAI API Key')

main_page()
