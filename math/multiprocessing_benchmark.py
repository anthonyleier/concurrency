import time
from concurrent.futures import ProcessPoolExecutor, ThreadPoolExecutor


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
    start_time = time.time()

    limit = 10_000_000
    num_processes = 10
    chunk_size = limit // num_processes

    with ProcessPoolExecutor(max_workers=num_processes) as executor:
        processes = []
        for i in range(0, limit, chunk_size):
            processes.append(executor.submit(count_primes_in_range, i, min(i + chunk_size, limit)))

        total_primes = sum(p.result() for p in processes)

    end_time = time.time()
    duration = end_time - start_time

    print(f"With multiprocessing, execution took {duration} seconds and obtained the result of {total_primes} prime numbers")


if __name__ == "__main__":
    main()
