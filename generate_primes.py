def generate_primes(n):
    primes = []
    for num in range(2, n+1):
        for i in range(2, num):
            if (num % i) == 0:
                break
        else:
            primes.append(num)
    return primes

n = 10  # example value
print(generate_primes(n))  # output: [2, 3, 5, 7, 11, 13, 17, 19]
