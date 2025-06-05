from abc import ABC, abstractmethod
import math

# Абстрактний клас Shape
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass  # Абстрактний метод, який мають реалізувати нащадки

# Клас Rectangle — наслідує від Shape
class Rectangle(Shape):
    def __init__(self, length, width):
        self.__length = length  # Приватне поле
        self.__width = width    # Приватне поле

    def get_length(self):
        return self.__length  # Геттер для length

    def get_width(self):
        return self.__width  # Геттер для width

    def area(self):
        return self.__length * self.__width  # Реалізація обчислення площі

# Клас Circle — наслідує від Shape
class Circle(Shape):
    def __init__(self, radius):
        self.__radius = radius  # Приватне поле

    def get_radius(self):
        return self.__radius  # Геттер для radius

    def area(self):
        return math.pi * self.__radius ** 2  # Реалізація обчислення площі

# Основна частина програми — демонстрація поліморфізму
def main():
    shapes = [
        Rectangle(4, 5),
        Circle(3),
        Rectangle(2, 10),
        Circle(1)
    ]

    for shape in shapes:
        print(f"Площа фігури {shape.__class__.__name__}: {shape.area():.2f}")

if __name__ == '__main__':
    main()
