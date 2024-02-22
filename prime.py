'''
* Trial Division algorithm not fast but not allocates lot of memory.
It has two for loops and divides each of the elements to check.
But it doesn't have two lists to store the different values.

* Sieve of Eratosthenes algorithm so fast but it uses memory lot.
It has list of bools same amount of the limit and prime list.
It doesn't have to divide each item in each for loop to each other to
find the value is prime or not.
It turns the False of the multiples of prime and adds it to prime list.
So it uses two list to store the values but it is fast.

* Dijkstra's Algorithm is avarege of two algorithm. It is not faster than
erathos but uses memory less than erathos, it is faster than trial division
but uses more memory than trial.

https://www.youtube.com/watch?v=fwxjMKBMR7s

'''

import time
import heapq
import sys

def trial_division(limit):
    primes = []
    for num in range(2, limit+1):
        is_prime = True
        for prime in primes:
            if prime > int(num**0.5):
                break
            if num % prime == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(num)

    space = sys.getsizeof(primes)
    print(f'Space: {space/1e6} MB')
    return primes

def sieve_of_eratos(n):
    primes = []
    sieve = [True] * (n + 1)
    for x in range(2, int(n**0.5) + 1):
        if sieve[x]:
            for y in range(x*x, n + 1, x):
                sieve[y] = False
    for x in range(2, n + 1):
        if sieve[x]:
            primes.append(x)
    space = sys.getsizeof(primes) + sys.getsizeof(sieve)
    print(f'Space: {space/1e6} MB')
    return primes

def dijkstra(n):
    primes_pool = [(4, 2)]
    heapq.heapify(primes_pool)
    primes = [2]
    for i in range(3, n+1):
        while primes_pool[0][0] < i:
            multiple, prime = heapq.heappop(primes_pool)
            heapq.heappush(primes_pool, (multiple + prime, prime))
        if primes_pool[0][0] == i:
            multiple, prime = heapq.heappop(primes_pool)
            heapq.heappush(primes_pool, (multiple + prime, prime))
        else:
            primes.append(i)
            heapq.heappush(primes_pool, (i*i, i))
    space = sys.getsizeof(primes) + sys.getsizeof(primes_pool)
    print(f'Space: {space/1e6} MB')
    return primes

# Example usage
limit = 1_000_000

print('---Trial Division---')
t1 = time.perf_counter()
trial_division(limit)
print(f'Time: {time.perf_counter()-t1} seconds\n')

print('---Sieve of Eratosthenes---')
t1 = time.perf_counter()
sieve_of_eratos(limit)
print(f'Time: {time.perf_counter()-t1} seconds\n')

print('---Dijkstra\'s Approach---')
t1 = time.perf_counter()
dijkstra(limit)
print(f'Time: {time.perf_counter()-t1} seconds\n')