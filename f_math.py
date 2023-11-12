import random

def digits(num: int) -> int:
    ''' Generate integer number with "num" digits '''

    str0 = "0123456789"
    str1 = "123456789"
    str2 = "23456789"
    res = ""

    if num == 1:
        str1 = str2  # start with digit 2

    for n in range(num):
        if res == "":
            res += random.choice(str1)  # the first digit is not 0
        else:
            res += random.choice(str0)

    return int(res)


def math_test(op: str, dig1: int, dig2: int) -> bool:
    '''
    Mathematical test

    op: operation "+", "-" or "x"
    dig1: number of digits for the first argument
    dig2: number of digits for the second argument
    '''

    a1 = digits(dig1)
    a2 = digits(dig2)

    if op == "+":
        prompt = "%s + %s = "
    elif op == "-":
        prompt = "%s - %s = "
    elif op == "x":
        prompt = "%s x %s = "

    ans = input(prompt % (a1, a2))

    while not ans.isdigit():
        ans = input(prompt % (a1, a2))

    if op == "+":
        res = a1 + a2
    elif op == "-":
        res = a1 - a2
    elif op == "x":
        res = a1 * a2

    if res == int(ans):
        done = True
        print(" OK!  :)")
    else:
        done = False
        print(" Oops  :(\n Правильный ответ: %s" % res)

    return done


def divide() -> bool:
    ''' Divide test with integer results values '''

    a1 = random.randint(10,39)  # unknown
    a2 = random.randint(2,9)

    res = a1 * a2

    ans = input("%s : %s = " % (res, a2))

    while not ans.isdigit():
        ans = input("%s : %s = " % (res, a2))

    if a1 == int(ans):
        done = True
        print(" OK!  :)")
    else:
        done = False
        print(" Oops  :(\n Правильный ответ: %s" % a1)

    return done
