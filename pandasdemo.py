import pandas as pd

# Create a DataFrame
data = {
    "Name": ["Alice", "Bob", "Charlie"],
    "Age": [25, 30, 35],
    "City": ["Pune", "Mumbai", "Delhi"]
}
df = pd.DataFrame(data)

# View DataFrame
print(df)

# Select a column
print(df["Name"])

# Filter rows
print(df[df["Age"] > 28])

# Group and aggregate
print(df.groupby("City")["Age"].mean())
