x = 10

def add(*args):
    ans = sum(args)
    return ans

def multiply(*args):
    result = 1
    for num in args:
        result *= num
    return result

def power(a,b):
    return (a**b)