import pandas as pd

# Read the CSV file into a DataFrame
df = pd.read_csv('sales.csv')  # Replace 'your_sales_data.csv' with your actual file name

# Filter rows for the year 2022
df_2022 = df[df['Year'] == 2022]

# Calculate the total number of items sold in 2022
total_items_2022 = df_2022['NumberOfItems'].sum()

print(f'Total items sold in the year 2022: {total_items_2022}')

df_2023 = df[df['Year'] == 2023]

# Find the store with the maximum sales in 2023
max_sales_store = df_2023.loc[df_2023['NumberOfItems'].idxmax()]['StoreId']

print(f'The store with the maximum sales in 2023 is Store ID: {max_sales_store}')
