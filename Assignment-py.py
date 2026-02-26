def compare_numbers(a, b):
    if a % 2 == 0 and b % 2 == 0:
        return min(a, b)
    else:
        return max(a, b)

# Examples:
print(compare_numbers(4, 8))  # Both numbers are even, returns 4
print(compare_numbers(3, 5))  # Both numbers are odd, returns 5
print(compare_numbers(2, 7))  # One number is odd, returns 7
print(compare_numbers(6, 3))  # One number is odd, returns 6
