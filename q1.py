#Write a Python function `getPrimeNumbers(n)` which returns a list containing all prime numbers between 2 and _n_.  
#Create a helper function to determine if a particular number is prime and then use a comprehension to generate your list.

def getPrimeNumbers(n):
        return [num for num in range(2, n+1) if isPrimeNum(num)]
            
def isPrimeNum(num):
    if num <= 2:
        return False
    #Check if number is divisible by up to the square root of the numbers factors
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
                
    return True
    

n = 20
prime_nums = getPrimeNumbers(n)
print(prime_nums)
