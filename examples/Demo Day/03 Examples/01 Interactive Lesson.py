import pandas as pd
from matplotlib import pyplot as plt

st.title("An interactive lesson")

# Define the data
data = [[1, 50, 100, 5000],
        [2, 40, 100, 2000], 
        [3, 30, 100, 5000],
        [4, 20, 100, 4000],
        [5, 10, 100, 5000]]
df = pd.DataFrame(data, columns=['col1', 'col2', 'col3', 'col4'])

# Create columns to select the data
c1, c2, c3, c4 = st.columns(4)

c1.write("Consider a dummy dataset:")
c1.write(df)

x = c2.selectbox('Select x', df.columns)
y = c2.selectbox('Select y', df.columns)

if x==y:
    c3.error("x and y cannot be the same")
else:
    df_filtered = df[[x, y]]
    c3.write("Dynamically filtered dataframe:")
    c3.write(df_filtered)

    fig = plt.figure()
    plt.plot(df[x], df[y], 'or-')
    c4.pyplot(fig)
