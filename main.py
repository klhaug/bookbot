def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        return file_contents

def count_words(text):
    words = len(text.split())
    print(f"Found {words} total words")


def main(): 
    files = get_book_text('./books/frankenstein.txt')
    count_words(files)
    
main()

