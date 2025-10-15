from stats import count_words
from stats import count_characters
from stats import sort_list
import sys

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        return file_contents

def main(): 
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    files = get_book_text(sys.argv[1])
    char_count = count_characters(files)
    sorted_list = sort_list(char_count)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}")
    print("----------- Word Count ----------")
    count_words(files)
    print("-----------  Character Count ----------")

    for entry in sorted_list:
        print(f"{entry['char']}: {entry['num']}")

    print("============ END ============")

main()

