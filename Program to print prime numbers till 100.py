for num in range(2, 101):   # loop from 2 to 100
    is_prime = True         # assume number is prime
    
    for i in range(2, int(num**0.5) + 1):  # check divisibility
        if num % i == 0:
            is_prime = False
            break
    
    if is_prime:
        print(num)
