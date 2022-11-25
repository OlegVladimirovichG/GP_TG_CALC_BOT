from sympy import sympify
from decimal import Decimal

a = 0
b = 0
op = ''
expr = ''


def init(user_dict):
    global a, b, op, expr
    op = user_dict["operation"]
    match user_dict['calc_type']:
        case 'decimal':
            a = Decimal(user_dict["first_num"])
            b = Decimal(user_dict["second_num"])
            return calc()
        case 'complex':
            a = complex(user_dict["first_num"])
            b = complex(user_dict["second_num"])
            return calc()
        case 'free':
            expr = user_dict["expression"]
            return free_calc()


def calc():
    match op:
        case '*':
            return a * b
        case '/':
            return a / b
        case '+':
            return a + b
        case '-':
            return a - b


def free_calc():
    return f'{expr} = {sympify(expr.strip())}'
