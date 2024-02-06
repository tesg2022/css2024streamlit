import streamlit as st
import pandas as pd
import plotly.express as px


st.title('Cape Flats Aquifer water quality in Cape Town')  # Sets the title of your page
st.header('Data Visualization Section')  # Sets a header for a section
st.subheader('Subsection: Bar Chart Analysis')  # Sets a subheader for a subsection

st.text('This section focuses on data preprocessing.')
st.markdown('**This is some bold text**')

import pandas as pd

data = {
    'Cl': [45, 37, 89, 67],
    'Location': ['Philippi1', 'Philippi2', 'Philippi3', 'UWC4']
}
df = pd.DataFrame(data)

st.write(df)

# Display descriptive statistics of 'Cl'
st.write(df['Cl'].describe())

st.write(df['Cl'].info())

import matplotlib.pyplot as plt

x = ['45', '37', '89', '89']
y = ['Philippi1', 'Philippi2', 'Philippi3', 'UWC4']

plt.bar(x, y)
plt.title('title Chloride in Cape Flats Aquifer')
plt.xlabel('x Location')
plt.ylabel('y Cl')
plt.show()

