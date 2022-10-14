# !/usr/bin/env python3
# -*- coding: utf-8 -*-

def posled(n):
    result = set()
    if (n == 0):
        result.add("")
    for i in range(1, n + 1, 1):
        for item in posled(n - i):
            result.add("(" * i + ")" * i + item)
            result.add("(" * i + item + ")" * i)
            result.add(item + "(" * i + ")" * i)
    return result


def cout_cout(result):
    cout = 0
    b = {','}
    for b in result:
        cout += 1
    return cout


def prov_i_vipol(skobok):
    if skobok % 2 == 0:
        n = int(skobok / 2)
        print("Последовательности: ", posled(n))
        print("Количество правильных скобочных структур: ", cout_cout(posled(n)))
    else:
        print("Нет правильной последовательности")


if __name__ == '__main__':
    skobok = int(input("Введите количество скобок: "))
    prov_i_vipol(skobok)
