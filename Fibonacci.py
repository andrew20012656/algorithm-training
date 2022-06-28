def fibonacci(n):
    lst = [1]*n
    if n == 1 or n == 2:
        return 1
    for i in range(2,n):
        lst[i] = lst[i-2] + lst[i-1]
    return lst[n-1]
