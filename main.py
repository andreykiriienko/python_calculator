
operators = ('+', '-', '*', '/')


def quiz():
    num = None

    while num != int:
        temp = input('Введите число: ')
        try:
            if type(int(temp)) != int:
                print('Введите корректное значение')
            else:
                num = int(temp)
                return str(num)
        except Exception as e:
            print(f'ERROR: {e}')
            continue


def is_operator():
    value = None

    while value not in operators:
        temp = input('Введите оператор: ')
        try:
            if temp in operators:
                value = temp
                return value
            else:
                print('Введите корректное значение')
        except Exception as e:
            print(e)
            continue


def calculate(num1: str, num2: str, oper):
    try:
        if num1.isdigit() and num2.isdigit():
            if oper in operators:
                if oper == operators[0]:
                    return int(num1) + int(num2)
                elif oper == operators[1]:
                    return int(num1) - int(num2)
                elif oper == operators[2]:
                    return int(num1) * int(num2)
                elif oper == operators[3]:
                    return int(num1) / int(num2)
        else:
            raise Exception('num1 or num2 are not digit')

    except Exception as error:
        return f'На 0 делить нельзя: {error}'


number1 = quiz()
operator = is_operator()
number2 = quiz()

calc = calculate(num1=number1, num2=number2, oper=operator)

print(calc)
