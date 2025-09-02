import sys

from stats import get_num_words, get_num_chars, get_sorted_num_chars

def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()
        return file_contents

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    path = sys.argv[1]
    book_text = get_book_text(path)
    num_words = get_num_words(book_text)
    num_chars = get_num_chars(book_text)
    sorted_num_chars = get_sorted_num_chars(num_chars)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for num in sorted_num_chars:
        if (num['char'].isalpha()):
            print(f"{num['char']}: {num['num']}")
    print("============= END ===============")

if __name__ == "__main__":
    main()