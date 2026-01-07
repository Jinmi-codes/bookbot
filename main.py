from stats import get_book_text, count_words, count_chars, sorter
import sys





def main():
    count = count_chars(path1)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path1}")
    #print(get_book_text("./books/frankenstein.txt"))
    print( f"Found {count_words(path1)} total words")
    sorted = sorter(count)
    for dih in sorted:
        if dih['char'].isalpha():
            print(f"{dih['char']}: {dih['num']}")

if len(sys.argv) > 1:
    path1=sys.argv[1]
    try:
        main()
    except Exception as e:
        print(f"The folllowing error occured: \n{e}")
else:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)