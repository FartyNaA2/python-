import sys
from datetime import datetime

# Клас Logger для логування з міткою часу у заданий потік
class Logger:
    def __init__(self, stream=sys.stderr, time_format='%Y-%m-%d %H:%M:%S'):
        self.stream = stream
        self.time_format = time_format

    def log(self, message):
        timestamp = datetime.now().strftime(self.time_format)
        print(f'[{timestamp}] {message}', file=self.stream)

def main():
    # створюємо об’єкт класу Logger, який відповідатиме за логування повідомлень.
    logger = Logger(sys.stderr, '%Y-%m-%d %H:%M:%S')

    while True:
        try:
            user_input = input('> ')
            if user_input.strip().lower() == 'exit':
                break
            logger.log(user_input)
        except KeyboardInterrupt:
            print("\nЗавершення...")
            break

if __name__ == '__main__':
    main()
