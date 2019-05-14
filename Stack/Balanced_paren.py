from Stack import Stack


def is_match(p1, p2):
    if p1 == '(' and p2 == ')':
        return True
    elif p1 == '[' and p2 == ']':
        return True
    elif p1 == '{' and p2 == '}':
        return True
    else:
        return False


def is_paren_balanced(string):
    stack = Stack()
    is_balanced = True
    idx = 0

    while idx < len(string) and is_balanced:
        paren = string[idx]
        if paren in "([{":
            stack.push(paren)
        else:
            if stack.is_empty():
                is_balanced = False
            else:
                s = stack.pop()
                if not is_match(s, paren):
                    is_balanced = False
        idx += 1

    if stack.is_empty() and is_balanced:
        return True
    else:
        return False


if __name__ == '__main__':
    string1 = "()"
    string2 = "{([]})}"
    string3 = "{[{}]}()"
    string4 = "))"

    print(is_paren_balanced(string1))
    print(is_paren_balanced(string2))
    print(is_paren_balanced(string3))
    print(is_paren_balanced(string4))
