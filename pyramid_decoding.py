def decode(message_file):
    # Read the contents of the file
    with open(message_file, 'r') as file:
        lines = file.readlines()

    # Create a dictionary to store the number-word pairs
    number_word = {}
    for line in lines:
        parts = line.split()
        number = int(parts[0])
        word = ' '.join(parts[1:])
        number_word[number] = word

    # Find the maximum number in the list
    max_number = max(number_word.keys())

    # Generate the pyramid of words
    pyramid = []
    current = 1
    level = []
    for i in range(1, max_number + 1):
        level.append(number_word[i])
        if i == current:
            pyramid.append(level)
            level = []
            current += len(pyramid) + 1

    # Flatten the pyramid and return the decoded message
    decoded_message = ' '.join(word for level in pyramid for word in level)
    return decoded_message

# Example usage:
file_path = 'pyramid.txt'  # Replace with your file path
decoded_message = decode(file_path)
print(decoded_message)