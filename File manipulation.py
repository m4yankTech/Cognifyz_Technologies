import re
from collections import Counter

def count_word_occurrences(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()

    text = re.sub(r'[^\w\s]', '', text).lower()
    words = text.split()
    word_counts = Counter(words)
    sorted_word_counts = dict(sorted(word_counts.items()))

    for word, count in sorted_word_counts.items():
        print(f"{word}: {count}")

# Specify the path to your text file
file_path = r'C:\Users\Acer\OneDrive\Desktop\New Text Document.txt'

# Count word occurrences and display the results
count_word_occurrences(file_path)
