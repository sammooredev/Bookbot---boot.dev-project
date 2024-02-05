def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_book_word_count(text)
    count_letters_returned = count_letters(text)
    chars_sorted_list = chars_dict_to_sorted_list(count_letters_returned)
    
    print(f"--- Book Report of " + book_path + " ---")
    print(f"{num_words} were found in the document.")
    
    for item in chars_sorted_list:
        if not item["char"].isalpha():
            continue
        print(f"the '{item['char']}' character was found {item['num']} times")
    
    print("--- End Report ---")

def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_book_word_count(text):
    words = text.split()
    return len(words)

def chars_dict_to_sorted_list(num_chars_dict):
    sorted_list = []
    for ch in num_chars_dict:
        sorted_list.append({"char": ch, "num": num_chars_dict[ch]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list


def count_letters(text):
    chars = {}
    for c in text:
        lowered = c.lower()
        if lowered in chars:
                chars[lowered] += 1
        else:
             chars[lowered] = 1
    return chars

def sort_on(dict):
    return dict["num"]


main()