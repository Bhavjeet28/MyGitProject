# main.py
import helper

def process_text(file_path):
    """Reads a file and processes its text."""
    with open(file_path, 'r') as file:
        text = file.read()
    word_counts = helper.count_words(text)
    unique_words = helper.get_unique_words(text)
    return word_counts, unique_words

if __name__ == "__main__":
    file_path = "example.txt"
    word_counts, unique_words = process_text(file_path)
    print("Word Frequencies:", word_counts)
    print("Unique Words:", unique_words)
