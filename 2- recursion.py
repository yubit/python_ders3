

# 5 x 4 x 3 x 2 x 1
def faktoriyel(sayi):
    if sayi == 1:
        return 1
    else:
        return sayi * faktoriyel(sayi-1)


def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)


print(faktoriyel(5))
print(fibonacci(40))
