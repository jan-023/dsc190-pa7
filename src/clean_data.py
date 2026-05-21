import pandas as pd
import sys
from pathlib import Path

input_path = Path("data/raw/events.csv")
output_path = Path("data/clean/events.csv")

df = pd.read_csv(input_path)

# Drop rows with any missing fields
df_clean = df.dropna()

# Drop rows with invalid event_type
valid_events = ['click', 'login', 'scroll', 'view', 'purchase']
df_clean = df_clean[df_clean["event_type"].isin(valid_events)]

# Drop rows with non-positive integer duration_seconds
print(type(df_clean["duration_seconds"][0]))
df_clean = df_clean[
        (df_clean["duration_seconds"] > 0) &
        (df_clean["duration_seconds"] % 1 == 0)
        ]
print(df_clean["duration_seconds"].dtype)

# Normalize timetamp to ISO8601 (YYYY-MM-DDTHH:MM:SS)
timestamp = df_clean["timestamp"]
## Case 1: rows of format YYYY-MM-DD HH:MM:SS
timestamp_cleaned = pd.to_datetime(timestamp, errors="coerce") 

## Case 2: rows of format YYYY-MM-DDTHH:MM:SS
## ex) 2026-01-19T18:57:56 
reformat_time = timestamp[timestamp_cleaned.isna()]
reformat_time = pd.to_datetime(reformat_time,
                              format="%Y-%m-%dT%H:%M:%S",
                              errors="coerce")
timestamp_cleaned.loc[reformat_time.index] = reformat_time

## Case 3: rows of format YYYY-MM-DDTHH:MM:SS.FFF
reformat_time = timestamp[timestamp_cleaned.isna()]
reformat_time = pd.to_datetime(reformat_time,
                               format="%Y-%m-%dT%H:%M:%S.%f",
                               errors="coerce")
timestamp_cleaned.loc[reformat_time.index] = reformat_time

## Case 4: rows of format MM/DD/YYYY HH:MM:SS
## Ex) 01/25/2026 06:45:26
reformat_time = timestamp[timestamp_cleaned.isna()]
reformat_time = pd.to_datetime(reformat_time,
                               format="%m/%d/%Y %H:%M:%S",
                               errors="coerce")
timestamp_cleaned.loc[reformat_time.index] = reformat_time

## Convert all datetime values to ISO8601 format
timestamp_cleaned = timestamp_cleaned.dt.strftime("%Y-%m-%dT%H:%M:%S")
df_clean["timestamp"] = timestamp_cleaned

# Ensure output directory exists
output_path.parent.mkdir(parents=True, exist_ok=True)

# Save cleaned data
df_clean.to_csv(output_path, index=False)
