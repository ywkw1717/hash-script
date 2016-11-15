#coding: utf-8
import os
import hashlib

from math import fabs
from hash_data import lorem

number = 10000000000 #11桁
flag = ''

def check_digit(mynumber):
    sum = 0
    q = 0

    for i in range(11):
            n = fabs(i-10)
            n = int(n)
            p = mynumber[n:n+1]

            if i+1 >= 1 and i+1 <= 6:
                q = i + 1 + 1
            elif i+1 >= 7 and i+1 <= 11:
                q = i + 1 - 5
            p = int(p)
            sum = sum + (p * q)

    mo = sum % 11

    if mo <= 1:
        return 0
    else:
        return 11 - mo

while True:
    number_s = str(number)
    check = check_digit(number_s)
    realnumber = number_s + str(check)

    h = hashlib.sha1()
    h.update(realnumber)
    flag = h.hexdigest()
    print realnumber,' ',flag

    if flag == lorem:
        print 'Answer{', realnumber, '}'
        break
    else:
        number = number + 1

