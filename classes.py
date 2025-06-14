import sys  # Імпортується модуль sys для взаємодії з системними викликами (наприклад, вихід з програми)

# Оголошення класу Figure, який представляє геометричну фігуру
class Figure:
    # Конструктор класу, що ініціалізує ім'я, площу, периметр і розміри фігури
    def __init__(self, name, area):
        self.name = name          # Ім'я фігури
        self.area = area          # Площа фігури
        self.perimeter = 0        # Периметр (початково 0)
        self.a = 0                # Довжина сторони a 
        self.b = 0                # Довжина сторони b 

    # Метод для виводу імені фігури
    def print_name(self):
        print(self.name)

# Оголошення класу Area, що описує площу з одиницею виміру
class Area:
    # Конструктор класу, який ініціалізує площу і одиницю виміру
    def __init__(self, unit="cm2"):
        self.value = 0    # Значення площі (початково 0)
        self.unit = unit  # Одиниця виміру (за замовчуванням "cm2")

# Основна функція програми
def main():
    comon_area = Area()          # Створення об'єкта площі з одиницею виміру cm2
    f = Figure("f", 0)           # Створення фігури з іменем "f" і площею 0
    g = Figure("g", 0)           # Створення фігури з іменем "g" і площею 0
    f.print_name()               # Вивід імені фігури f
    g.print_name()               # Вивід імені фігури g

    print(f.__dict__)            # Вивід усіх атрибутів об'єкта f у вигляді словника
    print(g.__dict__)            # Вивід усіх атрибутів об'єкта g у вигляді словника

    return 0                     # Повернення 0 для завершення програми

# Умова для запуску основної функції, якщо скрипт виконується напряму
if __name__ == '__main__':
    sys.exit(main())             # Виклик функції main() і завершення програми з її результатом
