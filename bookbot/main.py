def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    # print(text)
    words = get_num_words(text)
    letters = get_num_letters(text)
    final_report(book_path, words, letters)

def get_book_text(path):
    with open(path) as f:
        return f.read()   
    
def get_num_words(text):
    words = text.split()
    return len(words)

def get_num_letters(text):
    letters_dict = {}
    filtered_string = filter(lambda x: x.isalpha(), text.lower())
    
    for letter in filtered_string:
        if letter in letters_dict.keys():
            letters_dict[letter] += 1
        else:
            letters_dict.update({letter: 1})
            
    return letters_dict

def final_report(path, total_words, dict_of_letters): 
    print(f"--- Begin report of {path} ---")
    print(f"{total_words} words found in the document", "", sep='\n')
    for letter, count in dict_of_letters.items():
        print(f"The '{letter}' character was found {count} times")
    print("--- End report ---")

main()