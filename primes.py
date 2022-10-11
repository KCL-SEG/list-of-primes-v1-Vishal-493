"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""

#def primes(number_of_primes):
 #   list = []
  #  newList = []
   # a = 0
    #for i in range(number_of_primes*5):
     #   z = i + 1
      #  for j in range(1, z):
       #     if i == 0 or j == 0:
        #        pass
         #   else:
          #      if i%j == 0:
           ##         a+=1
             #       continue
#        if a == 2:
 #           newList.append(i)
  #  newList.sort()
   # x = 0
  #  while x < number_of_primes:
   #     list.append(newList[x])
    #    x += 1
            
  #  return list
def primes(number_of_primes):
    list = []
    while 1:
        for i in range(2, 100):
            for j in range(2, i-2):
                if i%j == 0:
        list.append(primenumber)
        if len.list == number_of primes:
                       break
        else:
                continue
    return list
