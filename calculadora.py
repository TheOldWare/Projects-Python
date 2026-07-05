def calc():
    print("Welcome to my simple Calculator!")

    print("Use o operador: + para adição")
    print("Use o operador: - para subtração")
    print("Use o operador: * para multiplicação")
    print("Use o operador: / para divisão")

calc()


while True:
    calculation = input(">>>: ")
    result = eval(calculation)
    print(f"Result: {result}")