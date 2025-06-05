import sys

for line in sys.stdin:
    if line.strip():  # strip() прибирає пробіли, табуляцію, \n тощо
        print(line, end='')  # end='' щоб уникнути додаткових перенесень рядка
