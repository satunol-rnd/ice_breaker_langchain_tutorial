import os
from dotenv import load_dotenv

if __name__ == '__main__':
    load_dotenv()
    print('Hello, LongChain!')
    print(os.environ.get('APP_MODE_', "not found!"))
    print(os.environ['OPENAI_API_KEY'])