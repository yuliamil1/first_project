from dotenv import load_dotenv
import os

load_dotenv()


def print_author():
    author = os.getenv('AUTHOR')
    print(f"Автор проекта: {author}")


print_author()