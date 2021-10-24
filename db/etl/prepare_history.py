import csv
import json
import pandas as pd

history = pd.read_csv('../datasets_raw/dataset_knigi_1_NORM.csv')
history.drop(columns=['source_url'], inplace=True)
history.rename(columns={'event': 'event_type', 'dt': 'created_on'}, inplace=True)
history.to_csv("../datasets_prepared/history_prepared.csv", header=True,
               columns=["user_id", "book_id", "event_type", "created_on"], index = False, quoting=csv.QUOTE_NONNUMERIC)
