a = float(int(input('Введіть перше число')))
b = float(int(input('Введіть друге число')))
activate = input('Введіть дію (+ - * /): ')


if activate == '+':
    print(a + b)
elif activate == '-':
    print(a - b)
elif activate == '*':
    print(a * b)
elif activate == '/':
    print(a / b)
