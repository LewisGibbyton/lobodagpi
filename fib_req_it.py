def fibonacci_req(n): #postac rekurencyjna
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci_req(n-1) + fibonacci_req(n-2)

def fibonacci_it(n):
    if n == 0:
        return 0
    a, b = 0, 1 #F0 = a, F1 = 1
    for _ in range(n - 1):
            temp = a + b
            a = b
            b = temp
    return b

print(fibonacci_req(4))
print("----------------")
print(fibonacci_it(4))