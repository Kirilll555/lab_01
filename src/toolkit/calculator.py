def calc(v):
    s = v.split()
    n = len(s)
    while len(s) > 1:
        for i in range(n - 1):
            if s[i] in ['*', '/']:
                if s[i] == '*':
                    s[i-1] = float(s[i-1]) * float(s[i+1])
                    s.pop(i+1)
                    s.pop(i)
                    n = len(s)
                    break
                if s[i] == '/':
                    if float(s[i+1]) == 0.0:
                        return 'Error'
                    else:
                        s[i-1] = float(s[i-1]) / float(s[i+1])
                        s.pop(i+1)
                        s.pop(i)
                        n = len(s)
                        break
        if s.count('*') + s.count('/') == 0:
            for i in range(n - 1):
                if s[i] in ['+', '-']:
                    if s[i] == '+':
                        s[i - 1] = float(s[i - 1]) + float(s[i + 1])
                        s.pop(i + 1)
                        s.pop(i)
                        n = len(s)
                        break
                    if s[i] == '-':
                        s[i-1] = float(s[i - 1]) - float(s[i + 1])
                        s.pop(i+1)
                        s.pop(i)
                        n = len(s)
                        break
    return s

v = '-5 + 4'
print(calc(v))