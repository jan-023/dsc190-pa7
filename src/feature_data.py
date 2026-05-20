import sys
import pandas as pd

input_path = sys.argv[1]
output_path = sys.argv[2]

df = pd.read_csv(input_path)

# Add "duration_minutes" column
df["duration_minutes"] = df["duration_seconds"]/60

# Add "weekday" column
df["weekday"] = pd.to_datetime(df["date"]).dt.day_name()

# Save changed data to output folder
df.to_csv(output_path, index=False)
