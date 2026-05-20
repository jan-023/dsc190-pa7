import sys
import pandas as pd
from pathlib import Path

input_path = Path("data/transformed/events.csv")
output_path = Path("data/features/events.csv")

df = pd.read_csv(input_path)

# Add "duration_minutes" column
df["duration_minutes"] = df["duration_seconds"]/60

# Add "weekday" column
df["weekday"] = pd.to_datetime(df["date"]).dt.day_name()

# Ensure output directory exists
output_path.parent.mkdir(parents=True, exist_ok=True)

# Save changed data to output folder
df.to_csv(output_path, index=False)
