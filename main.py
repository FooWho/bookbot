from stats import count_words
from stats import count_characters
from stats import sorted_list


def get_book_text(book):
    with open(book, 'r') as f:
        text = f.read()
        return text
    

def main():
    book_text = get_book_text('books/frankenstein.txt')
    num_words = count_words(book_text)
    character_dict = count_characters(book_text)
    result = sorted_list(character_dict)

    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for item in result:
        if item["char"].isalpha():
            print(f"{item["char"]}: {item["num"]}")
    print("============= END ===============")
    

main()