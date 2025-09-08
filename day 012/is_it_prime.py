def is_prime(num):
    for n in range(num + 1):
        if num in [0, 1]:
            return False
        if n in [0, 1]:
            pass
        elif n == num:
            return True
        elif num % n == 0:
            return False

prime_count = 0
range_upper_limit = int(input("input upper limit for prime test: ")) + 1

for n in range(range_upper_limit):
    if is_prime(n):
        print(f"{n} is a prime")
        prime_count += 1
    # elif is_prime(n) == False:
    #     print(f"{n} is not a prime")
print(f"from 0 to {range_upper_limit - 1} there are {prime_count} prime numbers")