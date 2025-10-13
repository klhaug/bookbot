from stats import count_words
from stats import count_characters

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        return file_contents

def main(): 
    files = get_book_text('./books/frankenstein.txt')
    count_words(files)
    char_count = count_characters(files)
    print(char_count)

main()

