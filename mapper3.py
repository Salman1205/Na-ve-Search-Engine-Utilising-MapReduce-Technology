#!/usr/bin/env python3
import sys
import string
import json

# Function for preprocessing text
def preprocess_text(text):
    punctuations = string.punctuation
    text_without_punctuations = text.translate(str.maketrans('', '', punctuations))
    words = text_without_punctuations.lower().split()
    return words

# Load vocabulary from file with indexing
vocabulary = {}
with open("vocabulary1.txt", "r") as vocab_file:
    for idx, word in enumerate(vocab_file):
        vocabulary[word.strip()] = idx

# Process each line of input
for line in sys.stdin:
    try:
        # Preprocess the sentence
        sentence_words = preprocess_text(line.strip())
        
        # Filter sentence words using vocabulary
        sentence_words_filtered = [word for word in sentence_words if word in vocabulary]
        
        # Calculate TF for filtered words
        tf = {}
        total_words = len(sentence_words_filtered)
        for word in sentence_words_filtered:
            tf[word] = tf.get(word, 0) + 1
        
        # Calculate TF-IDF
        tfidf = {}
        for word, freq in tf.items():
            tfidf[word] = freq / total_words  # TF
        
        # Emit TF-IDF values with word indices
        for word, tfidf_value in tfidf.items():
            word_index = vocabulary[word]
            print(f"{word_index}\t{json.dumps(tfidf_value)}")
            
    except Exception as e:
        # Print any exceptions to stderr
        sys.stderr.write(f"Error in mapper: {str(e)}\n")

