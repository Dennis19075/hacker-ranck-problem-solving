def swap_case(s):
    result = ""
    for character in s:
        if character.islower():
            result += character.upper()
        elif character.isupper():
            result += character.lower()
        else:
            result += character
    return result

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)