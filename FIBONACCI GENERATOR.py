def generate_fibonacci(count):
    fibonacci_sequence = [0, 1]  # Initialize with the first two Fibonacci numbers
    for i in range(2, count):
        next_fibonacci = fibonacci_sequence[-1] + fibonacci_sequence[-2]  # Calculate the next Fibonacci number
        fibonacci_sequence.append(next_fibonacci)
    return fibonacci_sequence

# Example usage:
number_of_terms = 10
fibonacci_series = generate_fibonacci(number_of_terms)
print("Fibonacci Series:", fibonacci_series)
