from Stack import Stack


def isOperator(s):
    return s in "+-*/%^"


def calc(x, y, operator):
    if operator == "+":
        return x + y
    elif operator == "-":
        return x - y
    elif operator == "*":
        return x * y
    elif operator == "/":
        return x / y
    elif operator == "%":
        return x % y
    elif operator == "^":
        return x ^ y
    else:
        return False


def postfix_eval(expression):
    stack = Stack()

    for c in expression:
        if c.isnumeric():
            stack.push(int(c))
        elif isOperator(c):
            a = stack.pop()
            b = stack.pop()
            result = calc(b, a, c)
            stack.push(result)
        elif c == '(':
            continue
            l = list()
            while c != ')':
                l.append(c)
                stack.push(postfix_eval(l))

    return int(stack.get_peek())


if __name__ == '__main__':

    expression = list(map(str, input().rstrip().split()))

    print(postfix_eval(expression))
