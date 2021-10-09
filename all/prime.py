number = int(input("give me a number "))

def prime_checker(number):
    is_prime = True

    for i in range(2, number):

        if number % i == 0:
            print(f"It's not a prime number")

            is_prime = False

            break

    if is_prime:
        print(f"It's a prime number")
    n = int(input("Check this number: "))

prime_checker(number)