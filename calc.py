from sympy import sympify


def calc(a, b, op):
    match op:
        case '*':
            return a * b
        case '/':
            return a / b
        case '+':
            return a + b
        case '-':
            return a - b


def free_calc(expr):
    expr = expr.strip()
    return f'{expr} = {sympify(expr)}'
