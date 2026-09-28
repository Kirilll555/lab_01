try:
    from .errors import CalculatorError
except ImportError:
    from errors import CalculatorError

def tokenize(inp):
    tokens = []
    i = 0
    while i < len(inp):
        if inp[i] == ' ':
            i += 1
            continue
        elif inp[i].isdigit() or inp[i] == '.':
            num = ''
            while i < len(inp) and (inp[i].isdigit() or inp[i] == '.'):
                num += inp[i]
                i += 1
            tokens.append(num)
        else:
            tokens.append(inp[i])
            i += 1
    return tokens


def validate(tokens):
    if len(tokens) == 0:
        raise CalculatorError('Введено пустое выражение')
    for token in tokens:
        if token in ['+', '-', '*', '/']:
            continue
        try:
            float(token)
        except ValueError:
            raise CalculatorError('Введен недопустимый токен')
    if tokens[0] in ['+', '-', '*', '/']:
        raise CalculatorError('Бинарная операция введена в начале выражения')
    for i in range(len(tokens) - 1):
        if tokens[i] in ['+', '-', '*', '/'] and tokens[i + 1] in ['+', '-', '*', '/']:
            raise CalculatorError('Введено две операции подряд')
    if tokens[-1] in ['+', '-', '*', '/']:
        raise CalculatorError('Бинарная операция введена в конце выражения')
    for i in range(len(tokens) - 1):
        if tokens[i] == '/' and float(tokens[i + 1]) == 0.0:
            raise CalculatorError('Деление на ноль')



def calculate(inp):
    tokens = tokenize(inp)
    i = 0
    while i < len(tokens):
        if tokens[i] in ['+', '-']:
            if i == 0 or tokens[i-1] in ['+', '-', '*', '/']:
                if tokens[i] == '-':
                    tokens[i+1] = '-' + tokens[i+1]
                    tokens.pop(i)
                else:
                    tokens[i + 1] = '+' + tokens[i + 1]
                    tokens.pop(i)
            else:
                i += 1
        else:
            i += 1
    validate(tokens)
    while len(tokens) > 1:
        for i in range(len(tokens) - 1):
            if tokens[i] in ['*', '/']:
                if tokens[i] == '*':
                    tokens[i-1] = float(tokens[i-1]) * float(tokens[i+1])
                    tokens.pop(i+1)
                    tokens.pop(i)
                    break
                if tokens[i] == '/':
                    tokens[i-1] = float(tokens[i-1]) / float(tokens[i+1])
                    tokens.pop(i+1)
                    tokens.pop(i)
                    break
        if tokens.count('*') + tokens.count('/') == 0:
            for i in range(len(tokens) - 1):
                if tokens[i] in ['+', '-']:
                    if tokens[i] == '+':
                        tokens[i - 1] = float(tokens[i - 1]) + float(tokens[i + 1])
                        tokens.pop(i + 1)
                        tokens.pop(i)
                        break
                    if tokens[i] == '-':
                        tokens[i-1] = float(tokens[i - 1]) - float(tokens[i + 1])
                        tokens.pop(i+1)
                        tokens.pop(i)
                        break
    return float(tokens[0])
