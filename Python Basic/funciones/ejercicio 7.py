numbers = [-12,0,1,4,6,7,13,9,67]

def is_prime(number):
    if number < 2:
        return False

    for divisor in range(2,number):
        if number % divisor == 0:
            return False
    return True

def find_primes(numbers):
    primes = []

    for number in numbers:
        if is_prime(number):
            primes.append(number)

    return primes

print(find_primes(numbers))