
def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        return file_contents

def word_count(text):
    words = text.split()
    return len(words)

def count_characters(text):
    lowered_string = text.lower()
    character_counts = {}
    for string in lowered_string:
        if string in character_counts:
            character_counts[string] += 1
        else:
            character_counts[string] = 1
    return character_counts

file_contents = main()
character_counts = count_characters(file_contents)
print(character_counts)

