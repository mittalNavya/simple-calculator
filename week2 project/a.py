# 1. Import the library we need to read data
import pandas as pd

# 2. Load the dataset into a DataFrame (a table-like structure)
df = pd.read_csv("HR_Attrition.csv")

# 3. Check the shape - (rows, columns)
print("Shape of dataset:", df.shape)

# 4. Look at the first 5 rows to see what the data looks like
print(df.head())

# 5. Check the Attrition column - how many "Yes" vs "No"
print(df['Attrition'].value_counts())

# 6. Same thing but as percentages (easier to see the imbalance)
print(df['Attrition'].value_counts(normalize=True) * 100)

# 7. Make a simple bar chart of Attrition counts
import matplotlib.pyplot as plt

df['Attrition'].value_counts().plot(kind='bar', color=['skyblue', 'salmon'])
plt.title("Employee Attrition Count")
plt.xlabel("Attrition")
plt.ylabel("Number of Employees")
plt.show()