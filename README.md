
---

# Chatbot Python OpenAI

## Project Overview

This Python application integrates with the OpenAI API to facilitate real-time text generation using OpenAI's GPT models. It is designed to be flexible, supporting execution in a local Python environment as well as in Google Colab for cloud-based operations. This dual functionality allows users to leverage their local systems for development and testing, or utilize the cloud for enhanced accessibility and collaboration without any local setup.

## Features

- **AI Text Generation:** Engage in real-time text-based conversations with an AI model.
- **Session History Management:** Capture and review the history of interactions within the session.
- **Flexible Deployment:** Run the application locally using a Python script or remotely on Google Colab.

## Prerequisites

To run this application, you need:
- Python 3.7 or later.
- Access to the OpenAI API (requires an API key).

## Installation

### Local Setup

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/brunoaffonso/openai_python_chatbot.git
   cd openai_python_chatbot
   ```

2. **Create and Activate a Virtual Environment:**
   ```bash
   python -m venv venv
   # For Windows
   venv\Scripts\activate
   # For Unix or MacOS
   source venv/bin/activate
   ```

3. **Install Dependencies:**
   ```bash
   pip install openai python-dotenv
   ```

4. **Set Up Environment Variables:**
   - Create a `.env` file in the project root directory.
   - Add your OpenAI API key to this file:
     ```
     OPENAI_API_KEY='your_openai_api_key_here'
     ```

### Google Colab Setup

1. **Access Google Colab:**
   - Visit the [Google Colab](https://colab.research.google.com/drive/1VlfRrNUM_1MQkMRLQfq8C5Jyc2jQclOf?authuser=0#scrollTo=5t_9vNwLdKAw) and sign in to your Google account.

2. **Prepare the Notebook Environment:**
   - The notebook is pre-configured with the necessary code. Simply open the link provided and you will see the notebook titled 'OpenAI Python Chatbot'.

3. **Install Required Packages:**
   ```python
   !pip install openai
   ```

4. **API Key Configuration:**
   - Use the following secure method to input your API key, which ensures your API key is not exposed:
     ```python
     import os
     from getpass import getpass
     os.environ['OPENAI_API_KEY'] = getpass('Enter your OpenAI API key:')
     ```

5. **Familiarize Yourself with the Notebook:**
   - Read through the text cells to understand what each part of the code is doing. This will help you make the most out of your interaction with the AI.

## Usage

### Running Locally

1. **Start the Script:**
   - Run the script using:
     ```bash
     python chatbot.py
     ```

2. **Interact with the AI:**
   - Follow the prompts in the terminal to interact with the AI.

### Running on Google Colab

1. **Execute the Cells:**
   - Execute the cells sequentially to initialize the environment and start the session by following the play button on each cell.

## Limitations

- The application is intended for educational and development purposes and not optimized for production use without further modifications.
- Proper error handling and security practices are recommended especially when dealing with sensitive data.

## Contributions

Contributions to this project are welcome. Please fork the repository and submit pull requests with your suggested changes.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

---

This README was generated using AI.

---
