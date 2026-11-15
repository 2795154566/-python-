def safe_to_int(value, default=0):
    try:
        return int(value)
    except (ValueError, TypeError):
        return default


print(safe_to_int("123"))       # 123
print(safe_to_int("abc"))       # 0
print(safe_to_int(None))        # 0
print(safe_to_int("12.5", -1))  # -1
print(safe_to_int(25))          # 25


