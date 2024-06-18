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
```
7. Command above will update/create Pipfile.lock and add langchain as dependency.
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

Development: Build your applications using LangChain's open-source building blocks and components. Hit the ground running using third-party integrations and Templates.
Productionization: Use LangSmith to inspect, monitor and evaluate your chains, so that you can continuously optimize and deploy with confidence.
Deployment: Turn any chain into an API with LangServe.

[more...](https://python.langchain.com/v0.2/docs/introduction/)