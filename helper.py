# helper.py
def count_words(text):
    """Counts the frequency of words in a given text."""
    words = text.split()
    word_freq = {}
    for word in words:
        word = word.lower().strip(".,!?()[]{}:;\"')")
        if word:
            word_freq[word] = word_freq.get(word, 0) + 1
    return word_freq

def get_unique_words(text):
    """Returns a set of unique words from the text."""
    words = text.split()
    unique_words = set(word.lower().strip(".,!?()[]{}:;\"')") for word in words)
    return unique_words
