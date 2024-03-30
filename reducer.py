#!/usr/bin/env python3
import sys

# Set to store vocabulary
vocab = set()

# Read input from standard input
for line in sys.stdin:
    # Remove leading and trailing whitespace
    word = line.strip()
    # Add word to vocabulary set
    vocab.add(word)

# Emit vocabulary set
for word in vocab:
    print(word)

