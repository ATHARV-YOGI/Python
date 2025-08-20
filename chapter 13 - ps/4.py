def divisible5(n):
    if(n%5==0):
        return True
    return False

a = [1,2,3,4343,54545,3435]

f = list(filter(divisible5, a))

print(f)