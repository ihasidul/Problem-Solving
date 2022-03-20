def valid_parentheses(string):
    paren_list = list(string)
    n = 0
    print(paren_list)
    for paren in paren_list:
        if n == -1:
            return False
        if paren == "(":
            n = n + 1
        elif paren == ")":
            n = n - 1
    if n == 0:
        return True
    return False

