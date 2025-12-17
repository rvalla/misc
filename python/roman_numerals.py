import random as rd

rn = ["M", "D", "C", "L", "X", "V", "I"]
rv = [1000, 500, 100, 50, 10, 5, 1]

def look_for_symbol(symbol, roman_n):
    s_case = 0
    if symbol == roman_n[0]:
        for s in range(min(3,len(roman_n))):
            if not symbol == roman_n[s]:
                break
            else:
                s_case += 1
    else:
        if len(roman_n) > 1:
            if symbol == roman_n[1]:
                s_case = -1
    return s_case

def roman_to_decimal(symbol_index, roman_n):
    number = 0
    #print(symbol_index,end="   ")
    #print(rn[symbol_index],end="   ")
    #print(roman_n)
    if len(roman_n) > 0:
        symbol_places = look_for_symbol(rn[symbol_index], roman_n)
        offset = 1
        if symbol_index == 0 or symbol_index == 2 or symbol_index == 4:
            offset = 2
        if symbol_index == 6:
            return symbol_places * rv[symbol_index]
        else:
            if symbol_places > 0:
                number += symbol_places * rv[symbol_index]
                return number + roman_to_decimal(symbol_index, roman_n[symbol_places:])
            elif symbol_places < 0:
                number += rv[symbol_index]
                number -= rv[symbol_index+offset]
                return number + roman_to_decimal(symbol_index + 1, roman_n[2:])
            else:
                return number + roman_to_decimal(symbol_index + 1, roman_n)
    else:
        return number

def decimal_to_roman(symbol_index, decimal_n):
    number = ""
    quotient = decimal_n // rv[symbol_index]
    remainder = decimal_n % rv[symbol_index]
    offset = 1
    if symbol_index == 0 or symbol_index == 2 or symbol_index == 4:
        offset = 2
    if quotient < 4:
        for q in range(quotient):
            number += rn[symbol_index]
        if quotient == 0 and remainder >= (rv[symbol_index] - rv[symbol_index + offset]):
            number += rn[symbol_index+offset] + rn[symbol_index]
            remainder = remainder - (rv[symbol_index] - rv[symbol_index + offset])
    else:
        number += rn[symbol_index+offset] + rn[symbol_index]
    if symbol_index == 6 or remainder == 0:
        return number
    else:
        if remainder >= (rv[symbol_index] - rv[symbol_index + offset]):
            return number + decimal_to_roman(symbol_index, remainder)
        else:
            return number + decimal_to_roman(symbol_index + 1, remainder)

print("RUNNING ROMAN NUMERALS TEST", end="\n\n")
n = 0
for i in range(100):
    n += rd.randint(1,70)
    try:
        roman = decimal_to_roman(0, n)
        decimal = roman_to_decimal(0, roman)
        print("- " + str(n) + ": " + roman, end=" --> ")
        print(decimal, end=" ")
        if not n == decimal:
            print("!!!!!", end=" ")
        print("", end="\n")
    except Exception as e:
        print("Ouch: " + str(n), end="\n")
        print(e)
 
