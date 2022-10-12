"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""


def primes(number_of_primes):
    list = []
    while 1:
        for i in range(2, 100):
            for j in range(2, i):
                if j == i:
                    pass
                else:
                    if i%j == 0:
                        list.append(i)
            if len(list) == int(number_of_primes):
                break
            else:
                continue
        break
    return list
       
 
                
