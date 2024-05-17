#!/usr/bin/env python3
import sys
import json

# Read input from standard input
for line in sys.stdin:
    try:
        # Split the input line into article_id and tfidf_json
        article_id, tfidf_json = line.strip().split('\t')
        
        # Convert TF-IDF JSON string to dictionary
        tfidf_data = json.loads(tfidf_json)
        
        # Prepare the output line
        output_line = f"{article_id}\t{tfidf_json}\n"
        
        # Write the output line to standard output
        sys.stdout.write(output_line)
        
    except Exception as e:
        # Print any exceptions to stderr
        sys.stderr.write(f"Error in reducer: {str(e)}\n")

