from string import digits


def func_1(n):
    total = 0
    for i in range(n + 1):
        total += i
    return total

print(func_1(5))



def func_2(n_list):
    counter = 0
    for n in n_list:
        print(counter, n)
        counter += 1


func_2(["яблоко", "банан", "груша"])


def func_3(digits, p):
    total = 0
    for i in digits:
        total += i ** p
        p += 1
    return total

print(func_3([1, 2, 3, 4], 3))

def dig_pow(n, p):
    total = 0
    digits = [int(d) for d in str(n)]
    for i in digits:
        total += i ** p
        p += 1
    if total % n == 0:
        return total // n
    else:
        return -1
print(dig_pow(89,1))
