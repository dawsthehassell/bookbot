
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

def sort_on(character_counts):
    return character_counts["num"]

def list_of_dicts(character_counts):
    return [{"character": key, "num": value} for key, value in character_counts.items()]

def report_text(sorted_character_counts):
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{final_word_count} words were found in the document")
    print()
    for i in sorted_character_counts:
        if i["character"].isalpha():
            print(f"The '{i['character']}' character was found {i['num']} times.")
    print("--- End report ---")

file_contents = main()
character_counts = count_characters(file_contents)
final_word_count = word_count(file_contents)
sorted_character_counts = list_of_dicts(character_counts)
sorted_character_counts.sort(reverse=True, key=sort_on)

print(report_text(sorted_character_counts))
