def prime(number):
    is_prime = True
    if number == 0 or number == 1:
        print(f"{number} is not prime")
    for i in range(2, number):
        if number % i == 0:
            is_prime = False
            print(f"{number} is not prime")
            break
        if is_prime:
            print(f"{number} is prime")
            break


prime(0)
prime(1)
prime(2)
prime(3)
prime(4)
prime(5)
prime(6)
prime(7)

