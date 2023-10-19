def is_prime(num):
    if num < 2: return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def next_prime(num):
    while True:
        num += 1
        if is_prime(num):
            return num

while True:
    user_input = int(input("Enter a number to check for primality: "))
    if is_prime(user_input):
        print(f"{user_input} is a prime number.")
    else:
        print(f"{user_input} is not prime. The next prime number is {next_prime(user_input)}")
    if input("Do you want to continue testing (yes/no)? ").strip().lower() != "yes":
        break