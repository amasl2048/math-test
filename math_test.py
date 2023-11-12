#!/usr/bin/python3
# -*- coding: utf-8 -*-
'''
Тест по математике для школьников 7-9 лет

amasl2048 (at) gmail (dot) com
https://github.com/amasl2048/math-test
'''
import sys

import f_math as fm

NUMBER = 10
results = ""

print("Тренировка математики\n")
print("Реши правильно %d примеров" % NUMBER)
print("Правильно/Неправильно: 0/0")

ACTIONS = {
    "1": lambda: fm.math_test("+", 2, 1),
    "2": lambda: fm.math_test("+", 2, 2),
    "3": lambda: fm.math_test("-", 2, 1),
    "4": lambda: fm.math_test("x", 1, 1),
    "5": lambda: fm.math_test("x", 2, 1),
    "6": lambda: fm.divide()
}

txt = """\nВыбери номер теста:
'1' - тест на сложение  XX + X
'2' - тест на сложение  XX + XX
'3' - тест на вычитание XX - X
'4' - тест на умножение X * X
'5' - тест на умножение XX * X
'6' - тест на деление
'q' - выход"""


def run_test(process) -> str:

    ok = 0
    nok = 0
    res = ""

    while ok < (NUMBER + nok):

        done = process()

        if done:
            ok += 1
        else:
            nok += 1

        res = " Результат: %s/%s\n" % (ok, nok)
        print(res)

    print("!!! УРА! МОЛОДЕЦ :) !!!")
    return res


while True:

    print(txt)

    cmd = input("> ")

    if cmd in ACTIONS.keys():
        process = ACTIONS[cmd]  # command
        results += "Тест %s:" % cmd
    else:
        print(results)
        print("Ждем Вас снова!")
        sys.exit(0)

    results += run_test(process)
