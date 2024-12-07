
def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        return file_contents

def word_count(text):
    words = text.split()
    return len(words)

file_contents = main()
result = word_count(file_contents)
print(result)
