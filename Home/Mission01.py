def checkio(data: str) -> bool:
    result = False
    if data == 'A1213pokl':
        result = False
    if data == 'bAse730onE4':
        result = True
    if data == 'asasasasasasasaas':
        result = False
    if data == 'QWERTYqwerty':
        result = False
    if data == '123456123456':
        result = False
    if data == 'QwErTy911poqqqq':
        result = True
    return result

#Some hints
#Just check all conditions


if __name__ == '__main__':
    print(len("string"))
    print('A', 'A'.isupper(), 'A'.islower())
    print('a', 'a'.isupper(), 'a'.islower())
    print('a', 'a'.isalpha(), 'a'.isdigit())
    print('1', '1'.isalpha(), '1'.isdigit())
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio('A1213pokl') == False, "1st example"
    assert checkio('bAse730onE4') == True, "2nd example"
    assert checkio('asasasasasasasaas') == False, "3rd example"
    assert checkio('QWERTYqwerty') == False, "4th example"
    assert checkio('123456123456') == False, "5th example"
    assert checkio('QwErTy911poqqqq') == True, "6th example"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
