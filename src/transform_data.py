import sys
import pandas as pd
from pathlib import Path

input_path = Path("data/clean/events.csv")
output_path = Path("data/transformed/events.csv")

df = pd.read_csv(input_path)

# Add "date" column in YYYY-MM-DD format
df["date"] = pd.to_datetime(df["timestamp"],
                            format="%Y-%m-%dT%H:%M:%S")
df["date"] = df["date"].dt.date

# Ensure output directory exists
output_path.parent.mkdir(parents=True, exist_ok=True)

# Save transformed data to output csv
df.to_csv(output_path, index=False)
