import pandas as pd
df = pd.read_excel('Book1.xlsx')
print(df.head())

# Write data to an Excel file
df.to_excel('output.xlsx', index=False)  # index=False to exclude the index column
