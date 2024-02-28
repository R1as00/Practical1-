from datetime import date
a = open (f'{date.today()}txt', "w")
try:
    print("Введите список покупок:")
    while True:
        todo = input()
        if todo.lower()=='стоп':
            break
        a.write(todo + '\n')
finally:
    a.close()

