from stats import count_words
from stats import count_characters


def get_book_text(book):
    with open(book, 'r') as f:
        text = f.read()
        return text
    

def main():
    book_text = get_book_text('books/frankenstein.txt')
    num_words = count_words(book_text)
    character_dict = count_characters(book_text)

    print(f"Found {num_words} total words")
    print(character_dict)
    

main()