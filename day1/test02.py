def is_anagram(s1, s2):
    dict = {}
    for ch in s1:
        dict[ch] = dict.get(ch, 0) + 1
    for ch in s2:
        dict[ch] = dict.get(ch, 0) - 1
    
    return all(num == 0 for num in dict.values())

result = is_anagram("listen", "silent")  
