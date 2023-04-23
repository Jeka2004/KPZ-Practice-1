def prime_num_generator():
    yield 2
    prime_nums = [2]
    num = 3
    while True:
        is_prime = True
        for prime_num in prime_nums:
            if num % prime_num == 0:
                is_prime = False
                break
            if prime_num**2 > num:
                break
        if is_prime:
            prime_nums.append(num)
            yield num
        num += 2

prime_gen = prime_num_generator()
print(next(prime_gen))
print(next(prime_gen))
