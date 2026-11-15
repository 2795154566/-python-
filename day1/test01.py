def filter_numbers(numbers:list):
    result = sorted(nums * nums for nums in numbers 
        if nums > 0 and nums % 2 == 0)
    return result

numbers = [3, -2, 4, 7, 8, 0, -6, 2]
result = filter_numbers(numbers)
print(result)
