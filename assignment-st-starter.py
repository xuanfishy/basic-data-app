# import packages
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load data with caching to improve performance
@st.cache
def load_data():
    data = pd.read_csv('train.csv')
    return data

# Load the dataset
df = load_data()

# Display the app header
st.header('Titanic App by Xinyue Yu')

# Display the first 10 rows of the DataFrame
st.write(df.head(10))

# Plotting setup
fig, ax = plt.subplots(nrows=1, ncols=3, figsize=(15, 5))
sns.set(style="darkgrid")

# Plot a boxplot for ticket prices in each class
classes = df['Pclass'].sort_values().unique()  # Ensure classes are sorted
for i, cls in enumerate(classes):
    sns.boxplot(y=df[df['Pclass'] == cls]['Fare'], ax=ax[i])
    ax[i].set_xlabel(f'PClass = {cls}')
    ax[i].set_ylabel('Fare')

# Tight layout to handle subplot spacing
plt.tight_layout()

# Show the plot in Streamlit
st.pyplot(fig)