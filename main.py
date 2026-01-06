from stats import get_book_text, count_words, count_chars

path1="./books/frankenstein.txt"

def main():
    count = count_chars(path1)
    print(get_book_text("./books/frankenstein.txt"))
    print( f"Found {count_words(path1)} total words")
    print(count)

main()
