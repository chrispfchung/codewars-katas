def count(string):
    d = {}
    for char in string:
        if char in d:
            d[char] += 1
        else:
            d[char] = 1
    if string == {}:
        return {}
    return d
