import math  

def countPrimes(n: int) -> int:

    primeNumCounter = 0

    if n <= 2:
        return n

    for i in range(2, n):
        numberFromRange = i
        # print("number from range: " + str(numberFromRange))
        sqrtNumber = round(math.sqrt(numberFromRange))
        # print("WOT: " + str(sqrtNumber))
        
        if all(isNormChislo(n, index) for index in range(2,sqrtNumber+1)):
            primeNumCounter += 1
            print("inside: " + str(primeNumCounter))
            print("sqrtNumber: " + str(sqrtNumber))
            print("numberFromRange: " + str(numberFromRange))

    return primeNumCounter



def isNormChislo(n: int, index: int) -> bool:
    # print("N: " + str(n) + " index: " + str(index))
    if (n/index)%1 == 0:
        return True
    return False
