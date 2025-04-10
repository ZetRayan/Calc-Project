from math import floor


def main(input: str):
    try:
        input = input.replace(" ", "")
        operators = ['+', '-', '*', '/']
        
        if len(input)<3: 
            raise ValueError("Строка не является математической операцией")
        
        operator = ''
        operator_index = -1
        
        for _operator in operators:
            for index, char in enumerate(input):
                if char == _operator:
                    if operator == '':
                        operator = _operator
                        operator_index = index
                    else:
                        raise ValueError("В выражении больше одного оператора!")
                    
        if operator_index == -1:
            raise ValueError("формат математической операции не удовлетворяет заданию - два операнда и один оператор (+, -, /, *)! Операнды должны быть целыми числами от 0 до 10") 
        
        a = input[0:operator_index]
        b = input[operator_index+1:]
        
        if a == '' or b == '':
            raise ValueError("Отсутствует один из опперандов!")
        
        try:
            a = int(a)
            b = int(input[operator_index+1:])
        except ValueError:
            raise ValueError(f"Операнды должны быть целыми числами. {a} и {b} не являются целыми числами!")
        if a > 10 or b > 10:
            raise ValueError("Операнды должны быть целыми числами от 0 до 10")
            

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
