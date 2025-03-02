from stats import get_book_word_count
from stats import character_count
from stats import sort_on
import sys


def get_book_text(filepath):
    with open(filepath) as f:
        file_content = f.read()

    return file_content

def main():
    if len(sys.argv) < 2:
        print ("Use: python3 main.py <path_to_book>")
        sys.exit(1)
    path = sys.argv[1]
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    text = get_book_text(path)
    words_count = get_book_word_count(text)
    print("----------- Word Count ----------")
    print (f"Found {words_count} total words")
    print("--------- Character Count -------")
    char_count = character_count(text)
    char_count1 = []
    for char in char_count:
        if char.isalpha():
            char_count1.append({'letter':char, 'number':char_count[char] })
    char_count1.sort(reverse=True, key=sort_on)
    for char in char_count1:
        print(f"{char['letter']}: {char['number']}")
    print("============= END ===============")

main()

