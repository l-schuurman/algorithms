# This is an implementation of the Sieve of Eratosthenes
# Determines all prime numbers up to a value n

from math import ceil, sqrt

n = 1000001
prime = [0] * n

def Sieve():
        
    for i in range(2, ceil(sqrt(n))):
        if (prime[i] == 0):
            for j in range(i * i, n, i):
                prime[j] = 1
                    
Sieve()