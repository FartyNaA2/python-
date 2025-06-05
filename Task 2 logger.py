import sys
from datetime import datetime # Імпортуємо datetime для отримання поточної дати та часу

def log(message):
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S') # Отримуємо поточну дату й час у форматі 'рік-місяць-день години:хвилини:секунди'
    print(f'[{timestamp}] {message}', file=sys.stderr)

# Нескінченний цикл для зчитування введення користувача
while True:
    try:
        user_input = input('> ') # Зчитуємо рядок, введений користувачем
        if user_input.strip().lower() == 'exit': # Якщо користувач ввів "exit" виходимо з циклу
            break  # Завершуємо цикл
  
        log(user_input) 
    except KeyboardInterrupt:
        print("\nЗавершення...") # Повідомлення про завершення
        break
