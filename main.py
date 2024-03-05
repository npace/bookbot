import sys

def main():
    path = "books/frankenstein.txt"
    content = read_content(path)
    print(f"--- Begin report of {path} ---")
    print(f"{count_words(content)} words found in the document")
    print()
    letter_counts = count_letters(content)
    for tuple in letter_counts:
        print(f"The '{tuple[0]}' character was found {tuple[1]} times")
    print("--- End report ---")
    return 0

def read_content(path):
    with open(path) as f:
        return f.read()

def count_words(content):
    words = content.split()
    return len(words)

def count_letters(content):
    letters = {}
    for letter in content:
        key = letter.lower()
        if not key.isalpha():
            continue
        count = 1
        if key in letters:
            count = letters[key] + 1
        letters[key] = count
    sorted_items = sorted(letters.items(), reverse=True, key=lambda tup: tup[1])
    return sorted_items

if __name__ == '__main__':
    sys.exit(main())