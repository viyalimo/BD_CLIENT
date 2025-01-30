import flet as ft
from help_function.router import Router
import socket
import configparser
import os

# Функция для чтения конфигурационного файла
def read_config():
    """Читает конфигурационный файл и возвращает IP и порт клиента."""
    base_dir = os.path.dirname(os.path.abspath(__file__))  # Путь к текущему файлу
    filename = os.path.join(base_dir, "client_config.ini")  # Путь к конфигу

    if not os.path.exists(filename):
        raise FileNotFoundError(f"Файл конфигурации не найден: {filename}")

    config = configparser.ConfigParser()
    config.read(filename)

    try:
        client_ip = config["client"]["ip"].strip().strip('"').strip("'")  # Убираем кавычки
        client_port = int(config["client"]["port"])
    except KeyError as e:
        raise KeyError(f"Ошибка в конфигурационном файле: отсутствует ключ {e}")
    except ValueError:
        raise ValueError("Ошибка в конфигурационном файле: порт должен быть числом")

    return client_ip, client_port

def main(page: ft.Page):
    LG = Router(page)

if __name__ == "__main__":
    # Читаем конфиг
    try:
        client_ip, client_port = read_config()
    except Exception as e:
        print(f"Ошибка: {e}")
        exit(1)

    print(f"http://{client_ip}:{client_port}/")

    ft.app(
        target=main,
        view=ft.AppView.WEB_BROWSER,
        host=client_ip,
        port=client_port
    )

