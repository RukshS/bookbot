from pathlib import Path

def get_book_text(file_path: str | Path) -> str:
    file_contents = ""
    with open(file_path) as f:
        file_contents = f.read()
    
    return file_contents

def count_words(file_path: str | Path) -> int:
    content = get_book_text(file_path)
    word_list = content.split()

    return len(word_list)


def count_characters(file_path: str | Path) -> dict:
    content = get_book_text(file_path).lower()
    character_dict = dict()
    for chr in content:
        if chr not in character_dict:
            character_dict[chr] = 0
        character_dict[chr] += 1

    return character_dict

def sort_on(items):
    return items["num"]

def sort_dict(chr_dict: dict) -> list:
    char_list = []
    for key, value in chr_dict.items():
        char_list.append({"char": key, "num": value})
    
    char_list.sort(reverse=True, key=sort_on)

    return char_list