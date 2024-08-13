def main():
    with open("books/frankenstein.txt") as f:
        text = f.read().lower()

    num_words = len(text.split())
    chars_dict = {char: text.count(char) for char in set(text) if char.isalpha()}

    print(f"--- Begin report of books/frankenstein.txt ---")
    print(f"{num_words} words found in the document\n")

    for char, count in sorted(chars_dict.items(), key=lambda item: item[1], reverse=True):
        print(f"The '{char}' character was found {count} times")

    print("--- End report ---")


if __name__ == "__main__":
    main()
