"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""

def primes(number_of_primes):
    if number_of_primes > 0:
        list = []
        counter = 2
        while len(list) < number_of_primes:
            divisible_numbers = 0
            for i in range(counter):
                if counter % (i+1) == 0:
                    divisible_numbers += 1
            if divisible_numbers == 2:
                list.append(counter)
            counter += 1
        print(list)
    else:
        raise ValueError("Input must be a positive integer!")
    return list
