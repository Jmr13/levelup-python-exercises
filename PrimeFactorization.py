# Own solution
def primeFactorization(number):
    primeFactors = []
    for x in range(2, number):
        while(number % x == 0):
            number /= x
            primeFactors.append(x)
    print(primeFactors)
   
primeFactorization(630)

# Tutorial's solution
def get_prime_factors(number):
    factors = []
    divisor = 2

    while divisor <= number:
        if number % divisor == 0:
            factors.append(divisor)
            number = number
        else:
            divisor += 1
    return factors