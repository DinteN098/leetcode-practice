import pandas as pd

# Create a sample DataFrame
data = {'Name': ['Alice', 'Bob', 'Charlie'],
        'Value': [10, 20, 30]}
df = pd.DataFrame(data)

print("Original DataFrame:")
print(df)

# Modify a specific cell (e.g., change the 'Value' for 'Bob')
df.loc[df['Name'] == 'Bob', 'Value'] = 25

print("\nDataFrame after modifying value:")
print(df)
