def is_valid_brackets(s) -> bool:
    stack = []
    pairs = {
        ")":"(",
        "]":"[",
        "}":"{"
    }

    for char in s:
        if char in "({[":
            stack.append(char)
        else:
            if not stack:
                return False
            if stack[-1] != pairs[char]:
                return False
            
            stack.pop()

    return len(stack) == 0


print(is_valid_brackets("()[]{}"))
# True

print(is_valid_brackets("([{}])"))
# True

print(is_valid_brackets("(]"))
# False 

print(is_valid_brackets("([)]"))
# False

print(is_valid_brackets("((("))
# False

print(is_valid_brackets(""))
# True