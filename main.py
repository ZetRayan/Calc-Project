from math import floor


def main(input: str):
    try:
        input = input.replace(" ", "")
        
        if len(input)>3: 
            raise ValueError("формат математической операции не удовлетворяет заданию - два операнда и один оператор (+, -, /, *)! Операнды должны быть целыми числами от 0 до 9") 
        if len(input)<3: 
            raise ValueError("Строка не является математической операцией")
        
        a,operator,b = input
        if (a.isdigit() and b.isdigit()) == False:
            raise ValueError("Операнды должны быть целыми числами от 0 до 9")
        if operator not in ['+', '-', '*', '/']:
            raise ValueError("Оператор должен быть одним из: +, -, *, /")
        
        a,b = int(a) , int(b)
        if operator == '/' and b == 0: 
            raise ZeroDivisionError ("На 0 делить нельзя!")
        
        
        operations = {
            "+" : lambda a,b : a + b,
            "-" : lambda a,b : a - b,
            "*" : lambda a,b : a * b,
            "/" : lambda a,b : a / b,
        }
        return operations[operator](a, b)
        
    except Exception as e:
        print(f"Произошла ошибка: {e}")
        exit()


result = main(input("Input:\n"))
print (f"Output:\n{floor(result)}") 
