# Getting Started

## Setup IDE (VS Code)

1. install Python 3.11
2. install pip
3. install pipenv
```cmd
    pip install --user pipenv
```
4. Add Pipenv to Your PATH
```cmd
    export PATH="$HOME/.local/bin:$PATH"
    source ~/.bashrc
    pipenv --version
```
5. Create virtual environment. Make sure you're in root project then run:
```cmd
    pipenv shell
```
6. Install langchain framework
```cmd
    pipenv install langchain
    pipenv install langchain-openai
```
7. Command above will update/create Pipfile.lock and add above dependency.
8. For code formatter (optional)
```cmd
    pipenv install black
```
9. Setup python debuger:
    - Go to debug tab (CTRL + SHIFT + D)
    - Klick 'create a launch.json file' -> Python/Python Debugger -> Python FIle
    - /.vscode/launch.json will be created then open it
    - add configuration -> "envFile": "${workspaceFolder}/.env"
    - put a name and done!
10. You can now run/debug using button with .env loaded
11. To load environtment variable dynamically in program, install bellow package:
```cmd
    pipenv install python-dotenv
```
12. Now if you run ```python ice_breaker.py```, you will get .env loaded

<br><br>

# About LangChain 🦜️🔗

## What Is LangChain ?

LangChain is a framework for developing applications powered by large language models (LLMs).

LangChain simplifies every stage of the LLM application lifecycle:

- <b>Development</b> : Build your applications using LangChain's open-source building blocks and components. Hit the ground running using third-party integrations and Templates.
- <b>Productionization</b> : Use LangSmith to inspect, monitor and evaluate your chains, so that you can continuously optimize and deploy with confidence.
- <b>Deployment</b> : Turn any chain into an API with LangServe.

[more...](https://python.langchain.com/v0.2/docs/introduction/)

## LangChain key features

LangChain is a framework designed for developing applications that rely on language models. It provides tools and abstractions to facilitate tasks like chaining together language model prompts, managing conversational context, and integrating language models with other data sources and tools.

Key features of LangChain include:

- <b>Prompt Management</b>: Helps in creating, storing, and managing prompts (text input) for language models.
- <b>Chaining</b>: Enables chaining of multiple language model calls together to build more complex applications.
- <b>Context Management</b> : Allows for maintaining and utilizing conversational context across multiple interactions.
- <b>Integrations</b> : Provides support for integrating with other tools and data sources, such as APIs and databases.

# About Large Language Models (LLMs)

LLM stands for "Large Language Model." These are advanced artificial intelligence models trained on vast amounts of text data to understand and generate human-like text. They are capable of performing a wide range of language-related tasks, such as text generation, translation, summarization, question answering, and more.

## Key Features of LLM

- <b>Training Data</b> : LLMs are trained on diverse and extensive datasets that include books, articles, websites, and other text sources. This broad training enables them to understand and generate text on various topics.

- <b>Deep Learning Architecture</b> : They typically use deep learning architectures like transformers. The transformer model, introduced in the paper "Attention is All You Need," is particularly popular for its effectiveness in handling language tasks.

- <b>Contextual Understanding</b> : LLMs can understand the context of words and sentences, allowing them to generate coherent and contextually appropriate text.

- <b>Scalability</b> : The "large" aspect refers to the model size, often involving billions of parameters. Larger models generally perform better due to their ability to capture more nuanced patterns in the data.

## Examples of Large Language Models
1. GPT-3 and GPT-4: Developed by OpenAI, these models are among the most well-known LLMs. They can generate text, answer questions, write code, and perform many other language tasks.

2. BERT (Bidirectional Encoder Representations from Transformers): Developed by Google, BERT is used primarily for understanding the context of words in search queries.

3. T5 (Text-to-Text Transfer Transformer): Another model by Google that treats every NLP problem as a text-to-text task, enabling it to handle a wide range of language processing tasks.

4. LaMDA (Language Model for Dialogue Applications): Also by Google, this model is designed specifically for dialogue applications, focusing on generating more natural and engaging conversations.

## Applications of LLMs

- Text Generation: Writing articles, stories, and other creative content.
- Customer Support: Automated chatbots that can understand and respond to customer queries.
- Code Generation: Assisting programmers by generating code snippets or entire programs.
- Translation: Converting text from one language to another with high accuracy.
- Summarization: Condensing long texts into shorter summaries while retaining key information.
- Sentiment Analysis: Determining the sentiment or emotion expressed in a piece of text.

## Working with LLMs

When working with LLMs, developers often use APIs provided by organizations like OpenAI, Google, or Hugging Face. These APIs allow easy integration of LLM capabilities into applications without needing to manage the underlying model infrastructure.