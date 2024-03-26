def decorator(numbers):
    def print_results(x):
        print(numbers(x))
    return print_results

@decorator
def numbers(x):
    return x**2

numbers(2)