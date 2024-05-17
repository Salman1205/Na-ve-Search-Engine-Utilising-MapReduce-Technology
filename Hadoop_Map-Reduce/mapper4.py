#!/usr/bin/env python3
import sys
import json

# Read TF-IDF values from output3.txt
tfidf_output3 = {}
for line in open("output3.txt", "r"):
    try:
        parts = line.strip().split('\t')
        article_id = parts[0]
        tfidf_str = parts[1]
        tfidf_dict = json.loads(tfidf_str)
        tfidf_output3[article_id] = tfidf_dict
    except Exception as e:
        sys.stderr.write(f"Error in reading TF-IDF from output3.txt: {str(e)}\n")

# Read TF-IDF values from output4.txt and calculate the scalar product
for line in open("output4.txt", "r"):
    try:
        parts = line.strip().split('\t')
        index = parts[0]
        tfidf = float(parts[1])
        
        # Loop through the TF-IDF values of each article_id in output3.txt and calculate the scalar product
        for article_id, tfidf_dict in tfidf_output3.items():
            if index in tfidf_dict:
                scalar_product = tfidf_dict[index] * tfidf
                print(f"{article_id}\t{scalar_product}")
    except Exception as e:
        sys.stderr.write(f"Error in mapper: {str(e)}\n")

# To ensure the output is flushed to stdout
sys.stdout.flush()

