frankenstein_book = "books/frankenstein.txt" 

with open("books/frankenstein.txt") as f:
    book = f.read()
    book_name = f.name

def num_of_words(book):
    words = book.split()
    return len(words)

def letter_count(book):
    letters = {}
    for i in book.lower():
        if i not in letters:
            letters[i] = 1
        else:
            letters[i] += 1
    return letters

def create_report(book_name, book):
    print(f"--- Begin report of {book_name}")
    print(f"{num_of_words(book)} words found in the document\n\n")
    letters = [(key, value) for key, value in letter_count(book)].sort()
    print(letters)
    #for i in range(len(letters)):
     #   print(f"The {letters[0]} character was found {count[i]}")

create_report(book_name, book)
