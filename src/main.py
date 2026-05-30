print('Hello from repository!')
print('This is an update from my local machine!')
import os
from dotenv import load_dotenv

# Загружаем переменные окружения из .env
load_dotenv()

def print_author():
    # Читаем значение переменной AUTHOR из .env и присваиваем его переменной author
    author = os.getenv('AUTHOR')
    print(f"Автор проекта: {author}")

# Проверяем работу функции
print_author()



