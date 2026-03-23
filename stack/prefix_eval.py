def evaluate_prefix(expr):
    stack = []
    tokens = expr.split()[::-1]

    for token in tokens:
        if token.isdigit():
            stack.append(int(token))

        else:
            a = stack.pop()
            b = stack.pop()

            if token == '>':
                stack.append(a > b)
            elif token == '<':
                stack.append(a < b)
            elif token == '==':
                stack.append(a == b)
            elif token == 'and':
                stack.append(a and b)
            elif token == 'or':
                stack.append(a or b)

    return stack.pop()

expr = "and > 5 3 < 2 1"

print("Result:", evaluate_prefix(expr))

