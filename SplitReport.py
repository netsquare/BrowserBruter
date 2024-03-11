import pandas as pd
import sys

final_report = sys.argv[1]

# Read the CSV file into a pandas DataFrame
df = pd.read_csv(final_report)
row_limit = int(sys.argv[2])
# Split the DataFrame into chunks
chunks = [df[i:i+row_limit] for i in range(0, len(df), row_limit)]
# Write each chunk to a new CSV file
for i, chunk in enumerate(chunks):
    output_file = f"{final_report}_{i}.csv"
    chunk.to_csv(output_file, index=False)