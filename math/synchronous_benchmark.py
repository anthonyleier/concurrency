import time


def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


def count_primes_in_range(start, end):
    count = 0
    for i in range(start, end):
        if is_prime(i):
            count += 1
    return count


def main():
    start = time.time()
    limit = 10_000_000
    qty = count_primes_in_range(0, limit)
    end = time.time()
    duration = end - start
    print(f"With synchronous approach, execution took {duration} seconds and obtained the result of {qty} prime numbers")


if __name__ == "__main__":
    main()
