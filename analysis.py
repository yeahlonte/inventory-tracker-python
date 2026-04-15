import pandas as pd

# Load data
data = pd.read_csv("maintenance_data.csv")

# Convert dates
data["Open Date"] = pd.to_datetime(data["Open Date"])
data["Completed Date"] = pd.to_datetime(data["Completed Date"])

# Create repair time
data["Days Open"] = (data["Completed Date"] - data["Open Date"]).dt.days

print("\nRequests by Shop:")
print(data["Shop"].value_counts())

print("\nRequests by Location:")
print(data["Location / Area"].value_counts())

print("\nAverage Repair Time:")
print(data["Days Open"].mean())
