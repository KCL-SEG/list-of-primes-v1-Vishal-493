"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""

def primes(number_of_primes):
    list = []
    newList = []
    a = 0
    for i in range(number_of_primes*5):
        z = i + 2
        for j in range(0, z):
            if i == 0 or j == 0:
                pass
            else:
                if i%j == 0:
                    a+=1
                    continue
        if a == 2:
            newList.append(i)
    newList.sort()
    x = 0
    while x < number_of_primes:
        list.append(newList[x])
        x += 1
            
    return list
