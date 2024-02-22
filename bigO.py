########################## BIG O NOTATION ##############################
'''
- Time Complexity
- Space Complexity
- We use it to show the worst case.(Best Case - Avarage Case)

1- O(1) — Constant Time Complexity
2- O(log n) — Logarithmic Time Complexity
3- O(n) — Linear Time Complexity
4- O(n log n) — Linearithmic Time Complexity
5- O(n²) — Quadratic or Polinomial Time Complexity
6- O(2^n) — Exponential Time Complexity
7- O(n!) — Factorial Time Complexity

https://medium.com/@stefentaime_10958/understanding-big-o-notation-with-real-world-python-examples-a4ed435b8a56
'''


#! O(1) Constant Time Complexity
'''
Constant time complexity, denoted as O(1), means that the execution time
of an algorithm remains constant and does not depend on the size of the
input. In other words, the algorithm takes roughly the same amount of time
to complete, regardless of how large or small the input is.
'''
def get_first_element(numbers):
    return numbers[0]

numbers = [1, 2, 3, 4, 5, 6, 7]
first_element = get_first_element(numbers)
print(first_element)



#! O(log n) Logarithmic Time Complexity
'''
Logarithmic time complexity, denoted as O(log n), indicates that the
execution time of an algorithm grows logarithmically with the size of
the input. In other words, the algorithm's performance increases at a
decreasing rate as the input size grows. Algorithm with logarithmic
complexity are typically efficient, especially when dealing with large
input size, because the growth rate of their execution time is slower
than linear complexity (O(n)).
A common example of an algorithm with logarithmic time complexity is the
binary search algorithm. Here's a Python implementation of binary search.
'''
def binary_search(arr, target):
    low, high = 0, len(arr) - 1
    
    while low <= high:
        mid = (low + high) // 2
        
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1

numbers = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
target = 13
result = binary_search(numbers, target)
print(result) # index of target [6]



#! O(n) Linear Time Complexity
'''
Linear time complexity, denotoed as O(n), indicates that the execution
time of an algorithm grows linearly with the size of the input. In other
words, as the input size increases, the algorithm's performance is directly
proportional to the increase in the input size. Algorithm with linear complexity
are generally considered efficient for small to moderately sized input data.
A common example of an algorithm with linear time complexity is the linear
search algorithm. Here's a Python implementation of linear search:
'''
def linear_search(arr, target):
    for i, element in enumerate(arr):
        if element == target:
            return i 
    return -1

numbers = [5, 3, 1, 7, 9, 11, 13, 15, 17, 19]
target = 13
result = linear_search(numbers, target)
print(result) # index of target [6]



#! O(n log n) Linearithmic Time Complexity
'''
Linearitmich time complexity, denoted as O(n log n), indicates that the
execution time of an algorithm grows at a linear - algorithmic rate with
the size of the input. This means that as the input size increases, the
performance of the algorithm is impacted by both the input size (n) and the
logarithm of the input size (log n). Algorithm with linearithmic complexity
are generally considered efficient for large input data and are often seen
in sorting algorithms.
A common example of an algorithm with linearithmic time complexity is the
merge sort algorithm. Here's a Python implementation of merge sort:
'''
def merge(left, right):
    result = []
    i = j = 0
    
    while i < len(left) and j < len(right):
        if left[i] < right[i]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
        
        result.extend(left[i:])
        result.extend(right[i:])
        return result

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    
    return merge(left, right)

numbers = [5, 3, 1, 7, 9, 11, 13, 15, 17, 19]
sorted_numbers = merge_sort(numbers)
print(sorted_numbers)

'''
The merge sort algorithm's time complexity is O(n log n). This is due to
the algorithm repeatedly dividing the input list in half (log n divisions)
and then merging the sublists back together in linear time (n elements).
The complexity combination of these two steps results in the linearithmic
time complexity.
'''


#! O(n ** 2) Quadratic or Polinomial Time Complexity
'''
Quadratic time complexity, denoted as O(n ** 2), indicates that the execution
time of an algorithm grows quadratically with the size of the input. In other
words, as the input size increases, the performance of the algorithm is directly
proportional to the square of the input size. Algorithms with quadratic time
complexity are generally less efficient than those with linear or linearithmic
complexity, especially for large input sizes.
A common example of an algoritm with quadratic time complexity is the bubble
sort algorithm. Here's a Python implementation of bubble sort:
'''
def bubble_sort(arr):
    n = len(arr)
    
    for i in range(n):
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

numbers = [5, 3, 1, 7, 9, 11, 13, 15, 17, 19]
bubble_sort(numbers)
print(numbers)



#! O(2 ** n) Exponential Time Complexity
'''
Exponential time complexity, denoted as O(2 ** n), indicates that the 
execution time of an algorithm grows exponentially with the size of the
input. In other words, as the input size increases, the performance of the
algorithm doubles for each additional element in the input. Algorithm with
exponential complexity are generally considered inefficient for anything but
small input sizes, as their execution time increases very rapidly with larger
inputs.
A common example of an algorithm with exponential time complexity is the naive
recursive implementation of the Fibonacci sequence. Here's a Python
implementation of this approach:
'''
def naive_fibonacci(n):
    if n <= 1:
        return n
    else:
        return naive_fibonacci(n - 1) + naive_fibonacci(n - 2)

n = 10
result = naive_fibonacci(n)
print(result)



#! O(n!) Factorial Time Complexity
'''
Factorial time complexity, denoted as O(n!), indicates that the execution
time of an algorithm grows at a factorial rate with the size of the input.
In other words, as the input size increases, the performance of the algorithm
is directly proportional to the product of all positive integers up to input
size. Algorithms with factorial complexity are generally considered highly
inefficient, especially for larger input sizes, as their execution time
increases exremely rapidly.
A common example of an algorithm with factorial time complexity is the
brute-force solution to traveling salesman problem (TSP). Here's a 
Python implementation of this approach using itertools.permutations:
'''
import itertools

def tsp_brute_force(graph):
    n = len(graph)
    min_cost = float('inf')
    optimal_path = []
    
    for permutation in itertools.permutations(range(1, n)):
        cost = 0
        prev_city = 0
        for city in permutation:
            cost += graph[prev_city][city]
            prev_city = city
        cost += graph[prev_city][0]
        
        if cost < min_cost:
            min_cost = cost
            optimal_path = [0] + list(permutation) + [0]
        
        return min_cost, optimal_path
    
graph = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]
min_cost, optimal_path = tsp_brute_force(graph)
print('Minimum cost: ', min_cost)
print('Optimal path: ', optimal_path)