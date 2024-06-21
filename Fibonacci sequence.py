def generate_fibonacci(n):
    # Check if the number of terms is valid
    if n <= 0:
        print("Please enter a positive integer.")
    elif n == 1:
        print("Fibonacci sequence up to", n, "term:")
        print(0)
    else:
        print("Fibonacci sequence up to", n, "terms:")
        # Initialize the first two terms
        fib_sequence = [0, 1]
        while len(fib_sequence) < n:
            # Append the sum of the last two terms to the sequence
            fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
        
        # Print the Fibonacci sequence
        for term in fib_sequence:
            print(term, end=' ')
        print()

# Example usage
try:
    # Take input from the user
    num_terms = int(input("Enter the number of terms: "))
    generate_fibonacci(num_terms)
except ValueError:
    print("Invalid input! Please enter an integer.")
