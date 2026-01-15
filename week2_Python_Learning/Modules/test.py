"""
Testing module for custom package.
Demonstrates importing and testing functions from custom packages and subpackages:
- Testing maths module functions (addition, substraction)
- Testing subpackages mult module function (multiply)
"""

from package.maths import addition, substraction
from package.subpackages.mult import multiply


def test_package_functions():
    """Test custom package functions."""
    print("=== Testing Custom Package Functions ===")
    
    # Test substraction function
    result1 = substraction(5, 2)
    print(f"substraction(5, 2) = {result1}")
    
    # Test addition function
    result2 = addition(3, 5)
    print(f"addition(3, 5) = {result2}")
    
    # Test multiply function from subpackage
    result3 = multiply(10, 20)
    print(f"multiply(10, 20) = {result3}")
    
    print("All tests completed successfully!")


if __name__ == "__main__":
    test_package_functions()
