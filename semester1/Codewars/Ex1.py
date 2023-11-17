def digital_root(n):
    if n < 10:
        return n
    
    sum = 0
    while n > 0:
        sum += n % 10
        n //= 10
    
    return digital_root(sum)

n = 16

print(digital_root(n))