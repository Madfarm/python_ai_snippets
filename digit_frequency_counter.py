def digit_frequency(n):
    # Initialize an empty dictionary to store frequency of digits
    frequency_map = {}

    # Loop until n is greater than 0
    while n > 0:
        # Extract the last digit of n
        digit = n % 10

        # Update the frequency_map dictionary
        if digit in frequency_map:
            frequency_map[digit] += 1
        else:
            frequency_map[digit] = 1

        # Reduce n by removing its last digit
        n //= 10

    return frequency_map

# Example usage:
number = 122232323123434
result = digit_frequency(number)
print(f"Frequency of digits in {number}: {result}")