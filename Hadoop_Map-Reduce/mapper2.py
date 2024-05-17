#!/usr/bin/env python3
import sys
import re
import json

# Load vocabulary from distributed cache file
vocab = {}
with open("vocabulary.txt", "r") as vocab_file:
    for idx, word in enumerate(vocab_file):
        word = word.strip()
        vocab[word] = idx

# Regular expression to match article ID
article_id_pattern = re.compile(r'^(\d+)')

# Read input from standard input
article_id = None
section_text = ''
for line in sys.stdin:
    try:
        # Extract article ID
        match = article_id_pattern.match(line)
        if match:
            if article_id is not None:
                # Process the previous document
                words = section_text.split()
                # Calculate TF
                tf = {}
                total_words = len(words)
                for word in words:
                    if word in vocab:
                        word_index = vocab[word]
                        tf[word_index] = tf.get(word_index, 0) + 1
                
                # Calculate TF-IDF
                tfidf = {}
                for word_index, freq in tf.items():
                    tfidf[word_index] = freq / total_words  # TF
                    tfidf[word_index] *= 1 / len(tf)  # IDF
                
                # Prepare TF-IDF data as a dictionary
                tfidf_json = json.dumps(tfidf)
                
                # Emit article ID and TF-IDF JSON string
                print(f"{article_id}\t{tfidf_json}")
                
            # Start processing new document
            article_id = match.group(1)
            section_text = ''
        else:
            # Accumulate section text
            section_text += line.strip() + ' '

    except Exception as e:
        # Print any exceptions to stderr
        sys.stderr.write(f"Error in mapper: {str(e)}\n")

# Process the last document
if article_id is not None:
    words = section_text.split()
    # Calculate TF
    tf = {}
    total_words = len(words)
    for word in words:
        if word in vocab:
            word_index = vocab[word]
            tf[word_index] = tf.get(word_index, 0) + 1
    
    # Calculate TF-IDF
    tfidf = {}
    for word_index, freq in tf.items():
        tfidf[word_index] = freq / total_words  # TF
        tfidf[word_index] *= 1 / len(tf)  # IDF
    
    # Prepare TF-IDF data as a dictionary
    tfidf_json = json.dumps(tfidf)
    
    # Emit article ID and TF-IDF JSON string
    print(f"{article_id}\t{tfidf_json}")

