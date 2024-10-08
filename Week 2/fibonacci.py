def fibonacci(n):
    """
    Returns the nth number in the Fibonacci sequence.
    - O(n) time complexity
    - O(n) space complexity
    """
    fib = [0, 1]
    for i in range(2, n):
        fib.append(fib[i-1] + fib[i-2])
        
    return fib[n-1]