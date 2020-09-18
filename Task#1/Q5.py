def sieve(n):
    L = []
    for x in range(2,n + 1):
        L.append(x)
    primes = []
    while(len(L) > 0):
        num = L[0]
        primes.append(num)
        i = 0
        for numbers in L:
            if(numbers % num == 0):
                L.pop(i)
                # i = i - 1
            i = i + 1
    return primes

print(sieve(30))
