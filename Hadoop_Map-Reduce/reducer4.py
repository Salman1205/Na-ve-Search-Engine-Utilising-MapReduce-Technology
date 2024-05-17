#!/usr/bin/env python3
import sys

# Initialize variables to store the top 5 scalar products and corresponding article IDs
top_5_scalar_products = [-float('inf')] * 5
top_5_article_ids = [''] * 5
unique_article_ids = set()

# Read input from standard input
for line in sys.stdin:
    try:
        # Split the input line into article_id and scalar product
        article_id, scalar_product = line.strip().split('\t')
        scalar_product = float(scalar_product)
        
        # Check if the current scalar product is higher than any of the top 5
        if article_id not in unique_article_ids:
            for i in range(5):
                if scalar_product > top_5_scalar_products[i]:
                    # Shift down other values to make space for the new one
                    top_5_scalar_products[i+1:] = top_5_scalar_products[i:-1]
                    top_5_article_ids[i+1:] = top_5_article_ids[i:-1]
                    # Insert the new value
                    top_5_scalar_products[i] = scalar_product
                    top_5_article_ids[i] = article_id
                    break
            unique_article_ids.add(article_id)
                
    except Exception as e:
        sys.stderr.write(f"Error in reducer: {str(e)}\n")

# Output the top 5 article IDs with the highest scalar products
for article_id in top_5_article_ids:
    if article_id:
        print(article_id)

