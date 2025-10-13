def count_words(text):
    words = len(text.split())
    print(f"Found {words} total words")

def count_characters(text):
    char_dict = {}
    text_lowercase = text.lower()
    
    for char in text_lowercase:
        if char in char_dict:
            char_dict[char] += 1
        else:
            char_dict[char] = 1

    return char_dict
