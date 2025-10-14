from stats import count_words
from stats import count_characters
from stats import sort_list


def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        return file_contents

def main(): 
    files = get_book_text('./books/frankenstein.txt')
    char_count = count_characters(files)
    sorted_list = sort_list(char_count)
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    count_words(files)
    print("-----------  Character Count ----------")

    for entry in sorted_list:
        print(f"{entry['char']}: {entry['num']}")

    print("============ END ============")
main()

