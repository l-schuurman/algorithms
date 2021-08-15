# This is an implementation of the Sieve of Eratosthenes
# Determines all prime numbers up to a value n

# A list of integers from 1 to n are also factored to be squarefree
# Squarefree - no number is divisible by a perfect square (other than 1)
# Squarefree - the prime factorization has only unique factors

from math import ceil, sqrt

n = 1000001
prime = [0] * n
k = [i for i in range(n)]

def Sieve():
        
    for i in range(2, ceil(sqrt(n))):
        if (prime[i] == 0):
            for j in range(i * i, n, i):
                prime[j] = 1
                
                while (k[j] % (i * i) == 0):
                    k[j] //= (i * i)
                    
Sieve()