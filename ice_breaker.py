import os

if __name__ == '__main__':
    print('Hello, LongChain!')
    print(os.environ.get('APP_MODE_', "not found!"))
    print(os.environ['OPENAI_API_KEY'])