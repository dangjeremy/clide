# Import Dependencies
import numpy as np
import pandas as pd
import pickle

import sys
from os.path import dirname, join
import glob

CURRENT_DIR = dirname(__file__)
IN_FILE_DIR = join(CURRENT_DIR, "..\\data\\raw_data\\")
OUT_FILE_DIR = join(CURRENT_DIR, "..\\data\\processed_data\\")
list_of_dfs = []

# Loop over all csv files with glob
for file_count, file_path in enumerate(glob.glob(IN_FILE_DIR + "*.csv")):
    # Get the output file path for the input file (where we will save processed data)
    # file_name = file_path.split("\\")[-1]
    # OUT_FILE_DIR = join(CURRENT_DIR, "../data/processed_data/" + file_name)

    # Extract raw data
    df = pd.read_csv(file_path)
    # Add in Person ID Column. Unique ID for every file
    df.insert(1,"Person ID",file_count)
    # Remove any NaN's in question column as irrelevant
    df.dropna(subset=["question"], inplace=True)
    # Loop over each question number in the dataframe and append to list of dfs
    for question_number in df["question"].unique():
        print("Processing question",question_number,"for person",file_count)
        list_of_dfs.append(df[df["question"] == question_number])

print("Number of interactions processed:",len(list_of_dfs))

# Pickle the list of dfs
with open(OUT_FILE_DIR + "list_of_dfs.pickle", 'wb') as f:
    pickle.dump(list_of_dfs, f, protocol=pickle.HIGHEST_PROTOCOL)