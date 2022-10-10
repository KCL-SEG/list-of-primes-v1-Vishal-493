"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""

def primes(number_of_primes):
    list = []
    newList = []
    a = 0
    for i in range(100000000000000000000000000000000):
        for j in range(100000000000000000000000000000000):
            if j == 0:
                pass
            else:
                if i%j == 0:
                    a+=1
                    continue
    if factorCount == 2:
        newList.append(i)
    newList.sort()
    while x < number_of_primes:
        list.append(newList[x])
            
    return list
