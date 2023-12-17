def main():
    frankenstein_book = "books/frankenstein.txt" 
    with open(frankenstein_book) as f:
        book = f.read()
        book_name = f.name
    chars_dict = get_chars_dict(book)
    sorted_dict_to_list = chars_dict_to_sorted_list(chars_dict)
    print(f"--- Begin report of {book_name}")
    print(f"{num_of_words(book)} words found in the document\n\n")
    for item in sorted_dict_to_list:
        print(f"The '{item['char']}' character was found {item['num']} times")

def num_of_words(book):
    words = book.split()
    return len(words)

def get_chars_dict(book):
    letters = {}
    for i in book.lower():
        if i not in letters:
            letters[i] = 1
        else:
            letters[i] += 1
    return letters

def sort_key(d):
    return d["num"]

def chars_dict_to_sorted_list(num_chars_dict):
    sorted_list = []
    for ch in num_chars_dict:
        if ch.isalpha():
            sorted_list.append({"char": ch, "num": num_chars_dict[ch]})
    sorted_list.sort(key=sort_key, reverse=True)
    return sorted_list
   
main()