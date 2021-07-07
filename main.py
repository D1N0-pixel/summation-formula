import functools
from fractions import Fraction
from math import factorial, gcd

def combination(p, q):
    return factorial(p) // (factorial(p-q) * factorial(q))

def solution(n):
    if n == 1:
        return [1]
    result = [combination(n, i) for i in range(n)]
    for i in range(len(result) - 1):
        temp = list(map(lambda x: x * combination(n, i), solution(i+1)))
        for j in range(len(temp)):
            result[-1-j] -= temp[-1-j]
    result = list(map(lambda x: Fraction(x, combination(n, 1)), result))
    return result

def formula(n):
    num = solution(n)
    result = str()
    for i in range(len(num)):
        if num[i] == 0:
            continue
        if result and num[i].numerator > 0:
            result += ' + '
        elif result and num[i].numerator < 0:
            result += ' - '

        if num[i].denominator == 1:
            result += str(int(num[i]))
        else:
            result += f"{abs(num[i].numerator)}/{num[i].denominator}"
        if i == len(num) - 1:
            result += ' x'
        else:
            result += ' x^' + str(len(num) - i)
    return result

# ex
print(formula(3))
