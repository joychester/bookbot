file_contents = ""
with open("books/frankenstein.txt") as f:
    file_contents = f.read()

#print(f"{file_contents}")

def count_words(book):
    words = book.split()
    num_of_words = len(words)
    return num_of_words

#print(count_words(file_contents))

def count_letters(book):
    letters_dict = {}
    for letter in book:
        if letter.lower() in letters_dict:
            letters_dict[letter.lower()] += 1
        else:
            letters_dict[letter.lower()] = 1
    return letters_dict

#print(count_letters(file_contents))

def aggregate_report(count_words_result, count_letters_dict):
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{count_words_result} words found in the document")
    print("")
    sorted_keys = sorted(count_letters_dict, key=count_letters_dict.get, reverse=True)
    for ch in sorted_keys:
        if ch.isalpha():
            print(f"The '{ch}' character was found {count_letters_dict[ch]} times")
    print("--- End report ---")

count_words_result = count_words(file_contents)
count_letters_dict = count_letters(file_contents)
aggregate_report(count_words_result, count_letters_dict)