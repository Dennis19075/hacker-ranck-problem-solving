def sequence(n):
    """
    Returns a string with numbers from 1 to n using recursion
    Example: sequence(5) returns "12345"
    """
    # Base case: if n is 1, return "1"
    if n == 1:
        return "1"
    
    # Recursive case: get sequence for n-1, then add current number
    return sequence(n - 1) + str(n)


def golden_ratio_formula():
    """
    Calculate Golden Ratio using the mathematical formula: (1 + √5) / 2
    This is the most direct and accurate method.
    """
    import math
    return (1 + math.sqrt(5)) / 2


def fibonacci_recursive(n):
    """
    Calculate fibonacci number recursively
    Used to approximate golden ratio
    """
    if n <= 1:
        return n
    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)


def golden_ratio_fibonacci_recursive(n=30):
    """
    Approximate Golden Ratio using recursive Fibonacci ratio
    φ ≈ F(n+1) / F(n) as n approaches infinity
    
    Args:
        n: How many Fibonacci numbers to calculate (higher = more accurate)
    """
    if n < 2:
        return 1.0
    
    fib_n = fibonacci_recursive(n)
    fib_n_plus_1 = fibonacci_recursive(n + 1)
    
    return fib_n_plus_1 / fib_n


def golden_ratio_fibonacci_iterative(n=100):
    """
    More efficient version using iterative Fibonacci
    Can handle much larger n values
    """
    if n < 2:
        return 1.0
    
    # Calculate Fibonacci iteratively (much faster)
    a, b = 0, 1
    for _ in range(n - 1):
        a, b = b, a + b
    
    # Calculate F(n+1)
    fib_n = b
    fib_n_plus_1 = a + b
    
    return fib_n_plus_1 / fib_n


def golden_ratio_continued_fraction_recursive(depth=20):
    """
    Calculate Golden Ratio using recursive continued fraction
    φ = 1 + 1/(1 + 1/(1 + 1/(1 + ...)))
    
    This is a beautiful recursive definition of φ!
    """
    if depth <= 0:
        return 1.0
    
    return 1.0 + (1.0 / golden_ratio_continued_fraction_recursive(depth - 1))


def golden_ratio_newton_method(iterations=10):
    """
    Use Newton's method to solve x² - x - 1 = 0
    The positive solution is the golden ratio
    """
    # Starting guess
    x = 1.5
    
    for _ in range(iterations):
        # f(x) = x² - x - 1
        # f'(x) = 2x - 1
        # Newton's formula: x_new = x - f(x)/f'(x)
        x = x - (x*x - x - 1) / (2*x - 1)
    
    return x


def compare_golden_ratio_methods():
    """
    Compare different methods to calculate the golden ratio
    """
    print("=== GOLDEN RATIO CALCULATIONS ===\n")
    
    # True value for comparison
    true_phi = (1 + (5**0.5)) / 2
    print(f"True Golden Ratio: {true_phi:.10f}")
    print("-" * 40)
    
    # Method 1: Direct formula
    phi1 = golden_ratio_formula()
    print(f"1. Formula method:           {phi1:.10f}")
    print(f"   Error: {abs(phi1 - true_phi):.2e}")
    
    # Method 2: Fibonacci recursive (small n due to performance)
    phi2 = golden_ratio_fibonacci_recursive(20)
    print(f"2. Fibonacci recursive(20):  {phi2:.10f}")
    print(f"   Error: {abs(phi2 - true_phi):.2e}")
    
    # Method 3: Fibonacci iterative (can use larger n)
    phi3 = golden_ratio_fibonacci_iterative(50)
    print(f"3. Fibonacci iterative(50):  {phi3:.10f}")
    print(f"   Error: {abs(phi3 - true_phi):.2e}")
    
    # Method 4: Continued fraction
    phi4 = golden_ratio_continued_fraction_recursive(30)
    print(f"4. Continued fraction(30):   {phi4:.10f}")
    print(f"   Error: {abs(phi4 - true_phi):.2e}")
    
    # Method 5: Newton's method
    phi5 = golden_ratio_newton_method(10)
    print(f"5. Newton's method(10):      {phi5:.10f}")
    print(f"   Error: {abs(phi5 - true_phi):.2e}")


def golden_ratio_properties():
    """
    Demonstrate interesting properties of the golden ratio
    """
    phi = golden_ratio_formula()
    
    print("\n=== GOLDEN RATIO PROPERTIES ===")
    print(f"φ = {phi:.10f}")
    print(f"φ² = {phi**2:.10f}")
    print(f"φ + 1 = {phi + 1:.10f}")
    print(f"φ² - φ - 1 = {phi**2 - phi - 1:.10f} (should be ≈ 0)")
    print(f"1/φ = {1/phi:.10f}")
    print(f"φ - 1 = {phi - 1:.10f} (should equal 1/φ)")


# Test the functions
if __name__ == "__main__":
    print("Testing sequence function:")
    print(f"sequence(5) = {sequence(5)}")
    print(f"sequence(1) = {sequence(1)}")
    print(f"sequence(10) = {sequence(10)}")
    
    print("\n" + "="*50)
    
    # Test golden ratio functions
    compare_golden_ratio_methods()
    golden_ratio_properties()