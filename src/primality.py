# CSCI 1100 Gateway to Computer Science
#
# Some repetitive code relating to integers and primality.
#
import math

# isFactor : int * int -> boolean
def isFactor(m, n):
    return n % m == 0

# isPrime : int -> boolean
def isPrime(n):
    top = math.floor(math.sqrt(n)) + 1
    for i in range(2, top):
        if isFactor(i, n):
            return False
    return True

# removeComposites : int * list int -> list int 
def removeComposites(prime, ns):
    return [ n for n in ns if not(isFactor(prime, n))] 

# sieve : int -> int list       -- return list of all primes up to n.
def sieve(n):
    candidates = range(2, n + 1)
    primes = []
    while candidates != []:
        prime = candidates[0]
        primes.append(prime)
        candidates = removeComposites(prime, candidates)
    return primes

