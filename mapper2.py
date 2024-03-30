#!/usr/bin/env python3
import sys
import csv
import json

# Load vocabulary from distributed cache file
vocab = {}
with open("vocabulary1.txt", "r") as vocab_file:
    for idx, word in enumerate(vocab_file):
        word = word.strip()
        vocab[word] = idx

# Initialize a dictionary to store aggregated term frequencies for each article ID
aggregated_tf = {}

# Read input from standard input
for line in csv.reader(iter(sys.stdin.readline, '')):
    try:
        article_id, section_text = line
        words = section_text.split()  # Split the preprocessed text into words
        tf = {}
        for word in words:
            if word in vocab:
                word_index = vocab[word]
                tf[word_index] = tf.get(word_index, 0) + 1
        
        # If the article ID is not in the dictionary, add it with an empty dictionary as the value
        if article_id not in aggregated_tf:
            aggregated_tf[article_id] = {}
        
        # Update the aggregated term frequencies for the current article ID
        for word_index, count in tf.items():
            aggregated_tf[article_id][word_index] = aggregated_tf[article_id].get(word_index, 0) + count
            
    except Exception as e:
        # Print any exceptions to stderr
        sys.stderr.write(f"Error in mapper: {str(e)}\n")

# Emit the aggregated term frequencies for each article ID
for article_id, tf_values in aggregated_tf.items():
    tf_json = json.dumps(tf_values)
    print(f"{article_id}\t{tf_json}")

