import os
from dotenv import load_dotenv, find_dotenv

# Load environment variables from .env file
def load_env():
    _ = load_dotenv(find_dotenv())

# Retrieve OpenAI API key
def get_openai_api_key():
    load_env()
    return os.getenv("OPENAI_API_KEY")

# Retrieve Serper API key
def get_serper_api_key():
    load_env()
    return os.getenv("SERPER_API_KEY")

# Break lines every 80 characters without splitting words
def pretty_print_result(result):
    parsed_result = []
    for line in result.split('\n'):
        if len(line) > 80:
            words = line.split(' ')
            new_line = ''
            for word in words:
                if len(new_line) + len(word) + 1 > 80:
                    parsed_result.append(new_line)
                    new_line = word
                else:
                    new_line = word if not new_line else new_line + ' ' + word
            parsed_result.append(new_line)
        else:
            parsed_result.append(line)
    return "\n".join(parsed_result)
