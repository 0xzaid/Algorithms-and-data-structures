import random
import numpy as np


def miller_rabin(n, k):
    """
    function to find if number is prime or not using miller rabin algorithm

    Convert to binary
    Obtain mod values??
    Red values based on previous part 
    Repeated 

    LINE 16-18 IN PSEUDOCODE OF MILLER RABIN IN LECTURES IS VERY VERY IMPORTANT.    
    """
    if n % 2 == 0:
        prime = False
        return prime
    s, t = 0, n - 1
    while t % 2 == 0:
        s, t = s + 1, t // 2

    """
    optimise under this
    * cant be 64, instead use k = ln(n)
    """

    for i in range(64):
        a = random.randrange(1, n - 1)
        if power(a, n - 1, n) != 1:
            
            prime = "Composite!"
            return prime

        for i in range(1, s):
            modulo_n = power(a, (2 ** (i - 1) * t), n)
            if ((modulo_n ** 2) % n) == 1:
                if modulo_n != 1:
                    if modulo_n != n - 1:
                        
                        prime = "Composite!"
                        return prime
    
    prime = "Probably Prime!"
    return prime


def power(x, y, p):
    """
    function to perform modular exponentiation
    """
    res, x = 1, x % p
    while not (y <= 0):
        if y & 1:
            res = (res * x) % p
        y = y >> 1
        x = (x * x) % p
    return res

if __name__ == "__main__":
    # k = int(np.log(n))
    k = 64
    print(miller_rabin(9999999967, k))
    #print(power(2, 9234738910587316431890, 10))