#using the python code lambda function create a Fibonacci series from 1 to  50 elements?

from functools import reduce

# Lambda function to generate Fibonacci series
fib_series = lambda n: reduce(lambda x, _: x + [x[-1] + x[-2]], range(n - 2), [1, 1])

# Generate first 50 Fibonacci numbers
fib_50 = fib_series(50)

# Print the Fibonacci series
print(fib_50)
