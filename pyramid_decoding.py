def decode(message_file):
    with open(message_file, 'r') as file:
        lines = file.readlines()

    number_word = {}
    for line in lines:
        parts = line.split()
        number = int(parts[0])
        word = ' '.join(parts[1:])
        number_word[number] = word

    max_number = max(number_word.keys())

    pyramid = []
    current = 1
    level = []
    for i in range(1, max_number + 1):
        level.append(number_word[i])
        if i == current:
            pyramid.append(level)
            level = []
            current += len(pyramid) + 1

    decoded_message = pyramid[0][0]

    for i in range(1, len(pyramid)):
        decoded_message += ' ' + pyramid[i][-1]

    return decoded_message

# Example usage:
file_path = 'pyramid.txt' 
decoded_message = decode(file_path)
print(decoded_message)