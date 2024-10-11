import time
import asyncio


async def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


async def count_primes_in_range(start, end):
    count = 0
    for i in range(start, end):
        if await is_prime(i):
            count += 1
    return count


async def main():
    start_time = time.time()

    limit = 10_000_000
    num_tasks = 10
    chunk_size = limit // num_tasks

    tasks = []
    for i in range(0, limit, chunk_size):
        tasks.append(asyncio.create_task(count_primes_in_range(i, min(i + chunk_size, limit))))

    results = await asyncio.gather(*tasks)
    total_primes = sum(results)

    end_time = time.time()
    duration = end_time - start_time

    print(f"With asyncio, execution took {duration} seconds and obtained the result of {total_primes} prime numbers")

if __name__ == "__main__":
    asyncio.run(main())
