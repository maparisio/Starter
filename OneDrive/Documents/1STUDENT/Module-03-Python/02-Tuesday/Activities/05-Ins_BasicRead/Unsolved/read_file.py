file = '../Resources/input.txt'

# open file
with open(file, 'r') as text:
    print(text)

    lines = text.read()

    print(lines)

print("TThis is the first line.\nThis is the second line.|nThis is the last line.")
