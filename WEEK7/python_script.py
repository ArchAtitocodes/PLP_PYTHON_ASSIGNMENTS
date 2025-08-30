# Import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_iris

# Load the Iris dataset from sklearn
iris = load_iris()

# Convert the dataset into a pandas DataFrame
df = pd.DataFrame(iris.data, columns=iris.feature_names)

# Add species names as a categorical column
df['species'] = pd.Categorical.from_codes(iris.target, iris.target_names)

# -------------------------------
# Task 1: Explore the Dataset
# -------------------------------

# Display the first 5 rows to inspect the data
print(df.head())

# Show data types and non-null counts
print(df.info())

# Check for missing values in each column
print(df.isnull().sum())

# -------------------------------
# Task 2: Basic Data Analysis
# -------------------------------

# Display basic statistics for numerical columns
print(df.describe())

# Group data by species and calculate mean values
print(df.groupby('species').mean())

# -------------------------------
# Task 3: Data Visualization
# -------------------------------

# 1. Line Chart: Sepal length over index (simulated time series)
df['index'] = range(len(df))  # Create a simple index column
plt.plot(df['index'], df['sepal length (cm)'])
plt.title('Sepal Length Over Index')
plt.xlabel('Index')
plt.ylabel('Sepal Length (cm)')
plt.show()

# 2. Bar Chart: Average petal length per species
sns.barplot(x='species', y='petal length (cm)', data=df)
plt.title('Average Petal Length per Species')
plt.show()

# 3. Histogram: Distribution of sepal width
plt.hist(df['sepal width (cm)'], bins=15, color='lightblue', edgecolor='black')
plt.title('Sepal Width Distribution')
plt.xlabel('Sepal Width (cm)')
plt.ylabel('Count')
plt.show()

# 4. Scatter Plot: Sepal length vs petal length, colored by species
sns.scatterplot(x='sepal length (cm)', y='petal length (cm)', hue='species', data=df)
plt.title('Sepal vs Petal Length')
plt.show()
