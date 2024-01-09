def string_subsets(input_str):
    def backtrack(start, subset):
        result.append(''.join(subset))  # Append a copy of the current subset
        for i in range(start, len(input_str)):
            subset.append(input_str[i])  # Include the current character
            backtrack(i + 1, subset)  # Explore further with the updated subset
            subset.pop()  # Backtrack by removing the current character

    result = []
    backtrack(0, [])
    return result

# Example usage:
input_string = "abcd"
result = string_subsets(input_string)
print("Subsets of", input_string, ":", result)