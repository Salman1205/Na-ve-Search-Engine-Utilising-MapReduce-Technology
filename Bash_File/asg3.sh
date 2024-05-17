#!/bin/bash

# Step 1: Create directory and upload subset.csv
hadoop fs -mkdir -p /inputs/
hadoop fs -put /home/salman/Downloads/subset.csv /inputs/subset.csv

# Step 2: Run first MapReduce job to generate vocabulary.txt
hadoop jar /usr/local/hadoop-2.10.2/share/hadoop/tools/lib/hadoop-streaming-2.10.2.jar \
    -input /inputs/subset.csv \
    -output /inputs/output11 \
    -mapper mapper.py \
    -reducer reducer.py \
    -file /home/salman/Downloads/mapper.py \
    -file /home/salman/Downloads/reducer.py
hadoop fs -cat /inputs/output11/part-00000 > vocabulary.txt

# Step 3: Run second MapReduce job
hadoop jar /usr/local/hadoop-2.10.2/share/hadoop/tools/lib/hadoop-streaming-2.10.2.jar \
    -input /inputs/subset.csv \
    -output /inputs/output12 \
    -mapper mapper2.py \
    -reducer reducer2.py \
    -file /home/salman/Downloads/mapper2.py \
    -file /home/salman/Downloads/reducer2.py \
    -file /home/salman/Downloads/vocabulary.txt
hadoop fs -cat /inputs/output12/part-00000 > output3.txt

# Step 4: Run third MapReduce job
hadoop fs -put /home/salman/Downloads/input.txt /inputs/input.txt
hadoop jar /usr/local/hadoop-2.10.2/share/hadoop/tools/lib/hadoop-streaming-2.10.2.jar \
    -input /inputs/input.txt \
    -output /inputs/output13 \
    -mapper mapper3.py \
    -reducer reducer3.py \
    -file /home/salman/Downloads/mapper3.py \
    -file /home/salman/Downloads/reducer3.py \
    -file /home/salman/Downloads/vocabulary.txt
hadoop fs -cat /inputs/output13/part-00000 > output4.txt

# Step 5: Run fourth MapReduce job
hadoop jar /usr/local/hadoop-2.10.2/share/hadoop/tools/lib/hadoop-streaming-2.10.2.jar \
    -input /inputs/input.txt \
    -output /inputs/output14 \
    -mapper mapper4.py \
    -reducer reducer4.py \
    -file /home/salman/Downloads/mapper4.py \
    -file /home/salman/Downloads/reducer4.py \
    -file /home/salman/Downloads/output3.txt \
    -file /home/salman/Downloads/output4.txt
hadoop fs -cat /inputs/output14/part-00000 > result1.txt
