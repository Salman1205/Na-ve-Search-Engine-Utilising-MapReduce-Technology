#!/usr/bin/env python3
import sys
import json

# Read input from standard input
for line in sys.stdin:
    try:
        # Split the input line into article_id and TF-IDF JSON string
        article_id, tfidf_json = line.strip().split('\t')
        
        # Print the article ID and TF-IDF values
        print(f"{article_id}\t{tfidf_json}")
    except Exception as e:
        # Print any exceptions to stderr
        sys.stderr.write(f"Error in reducer: {str(e)}\n")

