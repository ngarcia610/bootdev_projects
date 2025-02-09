BOOK_PATH = "books/frankenstein.txt"

def print_book(path):
    with open(path) as f:
      return f.read()

def word_count(text):
    return len(text.split())

def char_count(text):
    char_dict = {
        'a': 0,
        'b': 0,
        'c': 0,
        'd': 0,
        'e': 0,
        'f': 0,
        'g': 0,
        'h': 0,
        'i': 0,
        'j': 0,
        'k': 0,
        'l': 0,
        'm': 0,
        'n': 0,
        'o': 0,
        'p': 0,
        'q': 0,
        'r': 0,
        's': 0,
        't': 0,
        'u': 0,
        'v': 0,
        'w': 0,
        'x': 0,
        'y': 0,
        'z': 0
    }
    text = text.lower()
    for word in text:
        for char in word:
            for key, value in char_dict.items():
                if key == char:
                    char_dict[key] += 1
    return char_dict

def nice_output(word_int, char_dict):
    print("--- Begin report of books/frankenstein.txt ---\n")

    # Print the word count
    print(f"{word_int} words found in the document.")

    # Sort the dictionary, reverse it so it's descending, and print each key, value
    sorted_dict = dict(sorted(char_dict.items(), key=lambda item: item[1], reverse=True))
    for key, value in sorted_dict.items():
        print(f"The {key} character was found {value} times.")

    print("\n--- End report ---")

book = print_book(BOOK_PATH)
words = word_count(book)
chars = char_count(book)

nice_output(words, chars)
