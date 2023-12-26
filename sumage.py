import pandas as pd

# Read the CSV file into a DataFrame
df = pd.read_csv('person.csv')

# Add all the numbers in the 'Age' column that are above 50
total_age_above_50 = df[df['Age'] <= 40]['Age'].sum()

print(total_age_above_50)