#!/usr/bin/env python3
import sys
import csv
import string

# Function for preprocessing text
def preprocess_text(text):
    punctuations = string.punctuation
    text_without_punctuations = text.translate(str.maketrans('', '', punctuations))
    words = text_without_punctuations.lower().split()
    return words

# Set to store vocabulary
vocab = set()

# Read input from standard input
for line in csv.reader(iter(sys.stdin.readline, '')):
    if len(line) == 2:  # Assuming CSV format: ARTICLE_ID in first column, SECTION_TEXT in second column
        _, section_text = line
        # Preprocess the text
        words = preprocess_text(section_text)
        # Add unique words to vocabulary set
        vocab.update(words)

# Emit vocabulary set
for word in vocab:
    print(word)

