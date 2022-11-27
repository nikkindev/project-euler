# Find prime factors. For each prime factor f, the probability of a number occuring
# in the sequence is (f-1)/f. Multiply it by the number d to get the total reducible fractions

# https://stackoverflow.com/questions/15347174/python-finding-prime-factors
def prime_factors(n):
    i = 2
    factors = set()
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.add(i)
    if n > 1:
        factors.add(n)
    return factors

d = 1000000
count = 0
for i in range(2,d+1):
    factors = prime_factors(i)
    running_count = i
    for factor in factors:
        running_count = running_count*(factor-1)//factor
    count += running_count
print(count)