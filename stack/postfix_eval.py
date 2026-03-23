def evaluate_postfix(expr):
    stack = []

    for token in expr.split():
        if token.isdigit():
            stack.append(int(token))
        else:
            b = stack.pop()
            a = stack.pop()

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



expr = "5 3 > 2 1 < and"
print("Result:", evaluate_postfix(expr))