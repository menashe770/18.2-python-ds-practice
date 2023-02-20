def valid_parentheses(parens):
    """Are the parentheses validly balanced?

        >>> valid_parentheses("()")
        True

        >>> valid_parentheses("()()")
        True

        >>> valid_parentheses("(()())")
        True

        >>> valid_parentheses(")()")
        False

        >>> valid_parentheses("())")
        False

        >>> valid_parentheses("((())")
        False

        >>> valid_parentheses(")()(")
        False
    """

    # stack = []

    # for p in parens:
    #     if p == '(':
    #         stack.append(p)
    #     elif p == ')':
    #         if not stack:
    #             return False
    #         else:
    #             stack.pop()

    # return len(stack) == 0

    count = 0

    for p in parens:
        if p == '(':
            count += 1
        elif p == ')':
            count -= 1

        # fast fail: too many right parens
        if count < 0:
            return False

    return count == 0

    # if parens.count('(') != parens.count(')'):
    #     return False
    # else:
    #     return True
