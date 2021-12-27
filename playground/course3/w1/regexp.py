def calculate(data, findall):
    matches = findall(r"([abc])([-+]?=)([abc]|[-+]?\d+)([-+]?\d+)?")  # Если придумать хорошую регулярку, будет просто
    for v1, s, v2, n in matches:  # Если кортеж такой структуры: var1, [sign]=, [var2], [[+-]number]
        if s == '=':
            if v2 not in ['a', 'b', 'c']:
                data[v1] = int(v2)
            else:
                data[v1] = data[v2] + int(n or 0)
        elif s[0] == '+':
            if v2 not in ['a', 'b', 'c']:
                data[v1] += int(v2) + int(n or 0)
            else:
                data[v1] += data[v2] + int(n or 0)
        else:
            if v2 not in ['a', 'b', 'c']:
                data[v1] -= int(v2) + int(n or 0)
            else:
                data[v1] -= data[v2] + int(n or 0)

    return data