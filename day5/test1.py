def reverse_words(s):
    reverse_list = [word for word in s.strip().split()]
    return " ".join(reversed(reverse_list))


print(reverse_words("hello world python"))
# "python world hello"

print(reverse_words("  I   love  Python  "))
# "Python love I"

print(reverse_words("hello"))
# "hello"

print(reverse_words(""))
# ""