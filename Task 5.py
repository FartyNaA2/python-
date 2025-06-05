import sys
from datetime import datetime

class Formatter:
    def format(self, message):
        raise NotImplementedError("Formatter must implement format method")

class TimeFormatter(Formatter):
    def __init__(self, time_format='%Y-%m-%d %H:%M:%S'):
        self.time_format = time_format

    def format(self, message):
        timestamp = datetime.now().strftime(self.time_format)
        return f"[{timestamp}] {message}"

class Handler:
    def handle(self, message):
        raise NotImplementedError("Handler must implement handle method")

class StreamHandler(Handler):
    def __init__(self, stream=sys.stderr):
        self.stream = stream

    def handle(self, message):
        print(message, file=self.stream)

class FileHandler(Handler):
    def __init__(self, file_path):
        self.file = open(file_path, 'a', encoding='utf-8')

    def handle(self, message):
        self.file.write(message + '\n')

    def __del__(self):
        self.file.close()

class Logger:
    def __init__(self, formatter: Formatter):
        self.formatter = formatter
        self.handlers = []

    def add_handler(self, handler: Handler):
        self.handlers.append(handler)

    def log(self, message):
        formatted = self.formatter.format(message)
        for handler in self.handlers:
            handler.handle(formatted)

def main():
    # Створюємо форматер
    formatter = TimeFormatter('%Y-%m-%d %H:%M:%S')

    # Створюємо логер з форматером
    logger = Logger(formatter)

    # Додаємо обробники: stderr і файл
    logger.add_handler(StreamHandler(sys.stderr))
    logger.add_handler(FileHandler("log.txt"))

    print("Введіть повідомлення для логування (введіть 'exit' для завершення):")
    while True:
        try:
            user_input = input("> ")
            if user_input.strip().lower() == 'exit':
                break
            logger.log(user_input)
        except KeyboardInterrupt:
            print("\nЗавершення програми...")
            break

if __name__ == "__main__":
    main()
