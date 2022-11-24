## **Measuring performance and Big O algorithm analysis:**

### **The `timeit` module:**
The `timeit` module is a handy built-in Python module that one can use to compute the time execution of a small block of code or small functions.
See the following example
```python
import timeit


def nth_fibonacci_number(n):
    """Returns the nth Fibonacci number."""
    if n <= 1:
        return n

    prevprev, prev, current = 0, 1, 1
    for _ in range(1, n):
        current = prevprev + prev
        prevprev = prev
        prev = current

    return current


print(timeit.timeit('nth_fibonacci_number(100)', number=100, globals=globals()))
```
By default, the `timeit.timeit()` function does not have access to variables and functions in the program. We must pass the `globals()` value as the key argument to solve this problem. The `number` key argument tells how many times the called block or function should be repeated. 

Example output (in seconds): 
```shell
0.00041310000233352184
```

---

### **The `cProfile` module:**
To analyse executed code more effectively, one can use the `cProfile` module, which is much more comprehensive and helpful than the `timeit` one.
```python
import cProfile


def nth_fibonacci_number(n):
    """Returns the nth Fibonacci number."""
    if n <= 1:
        return n

    prevprev, prev, current = 0, 1, 1
    for _ in range(1, n):
        current = prevprev + prev
        prevprev = prev
        prev = current

    return current


cProfile.run("nth_fibonacci_number(1_000_000)")
```
The output is as follows:
```shell
    4 function calls in 6.909 seconds

Ordered by: standard name

ncalls  tottime  percall  cumtime  percall filename:lineno(function)
    1    0.000    0.000    6.909    6.909 <string>:1(<module>)
    1    6.909    6.909    6.909    6.909 test.py:4(nth_fibonacci_number)
    1    0.000    0.000    6.909    6.909 {built-in method builtins.exec}
    1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
```

---

### **Big O analysis:**
The Big O is one of the most common types of analysis used to describe how the code slows down with increased data. One can distinguish 7 orders of Big O (from the fastest to the slowest):

- $O\big(1\big)$ - contant time of execution,
- $O\big(\log n\big)$ - time increases logarithmically,
- $O\big(n\big)$ - time increases linearly,
- $O\big(n\log n\big)$ - time increases logarithmically-linearly,
- $O\big(n^2\big)$ - time increases at a polynomial rate,
- $O\big(2^n\big)$ - time increases exponentially,
- $O\big(n!\big)$ - time increases at a factorial rate.

In general one can distinguish:
- Fast algorithms - $O\big(1\big)$ and $O\big(\log n\big)$.
- Moderate algorithms - $O\big(n\big)$ and $O\big(n\log n\big)$.
- Slow algorithms - $O\big(n^2\big)$, $O\big(2^n\big)$ and $O\big(n!\big)$.

How to interpret the Big O notation (on the example of a bookshelf and books):

* $O\big(1\big)$:  
  Determination if the shelf is empty or not has a constant time of execution. All you need is to look on the shelf.
* $O\big(\log n\big)$:  
  Searching for a book on an alphabetically arranged bookshelf. First, you check the book in the middle. Next, you check in the first half or second half of the shelf and so on.
* $O\big(n\big)$:  
  Searching for a book on a non-arranged bookshelf. You have to check all books to find the one.
* $O\big(n\log n\big)$:  
  Sorting books alphabetically. Think of it this way. First, you arrange one book. Then for the second book, you check if you place it before or after the first one - you follow the binary search and repeat that $n$ times.
* $O\big(n^2\big)$:  
  Searching for duplicates on non-arranged bookshelf. First, you take one book and check it with all others. For the second book, you make exactly the same and so on.
* $O\big(2^n\big)$:  
  Taking photos for each combination of books. Each book can be on the photo or not.
* $O\big(n!\big)$:  
  Taking photos of books in every possible order. Each possible order is a permutation. The number of these permutations is n! Think about it this way. For the first position on the shelf, you have n places. For the second position, you have n-1 places, then n-2 and so on. Such an operation gives n! choices.
