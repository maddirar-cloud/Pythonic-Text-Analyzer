from collections import Counter


def read_file(file_name):
    """Read and return the contents of the text file/whatever input file you have."""
    with open(file_name, "r") as file:
        return file.read()


def count_words(words):
    """Record the quantity of each respective word's appearances."""
    return Counter(words)


def find_long_words(words):
    """Return a list of words that have a higher character count than 3."""
    return [word for word in words if len(word) > 3]


def analyze_text(file_name):
    """Analyze a text file and print the respective frequency statistics."""
    text = read_file(file_name)
    words = text.lower().split()

    word_counts = count_words(words)
    long_words = find_long_words(words)

    print(f"The total number of words is: {len(words)}")
    print(f"The unique words count is: {len(word_counts)}")
    print("The most frequent words are:")

    for word, count in word_counts.most_common(5):
        print(f"'{word}': {count}")

    print(f"Long words (more than 3 characters): {len(long_words)}")


if __name__ == "__main__":
    analyze_text("sample.txt")
