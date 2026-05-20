import sys
import pandas as pd

input_path = sys.argv[1]
output_path = sys.argv[2]

df = pd.read_csv(input_path)

# Add "date" column in YYYY-MM-DD format
df["date"] = pd.to_datetime(df["timestamp"],
                            format="%Y-%m-%dT%H:%M:%S")
df["date"] = df["date"].dt.date

# Save transformed data to output csv
df.to_csv(output_path, index=False)
