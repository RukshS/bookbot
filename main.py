from pathlib import Path
from stats import count_words, count_characters, sort_dict
import sys

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]
    num_words = count_words(book_path)
    character_dict = count_characters(book_path)
    character_list = sort_dict(character_dict)

    print("============ BOOKBOT ============\n" \
    f"Analyzing book found at {book_path}")
    print(f"----------- Word Count ----------\nFound {num_words} total words")
    print("----------- Character Count ----------")
    for item in character_list:
        if not item['char'].isalpha():
            continue
        print(f"{item['char']}: {item['num']}")
    print("============= END ===============")


if __name__ == "__main__":
    main()