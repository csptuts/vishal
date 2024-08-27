import streamlit as st
import pandas as pd
# df = pd.DataFrame({
#   'first column': [1, 2, 3, 4],
#   'second column': [10, 20, 30, 40]
# })

# df

uploaded_file = st.file_uploader('Upload xlsx file')
if uploaded_file == None:
    st.stop()

df=pd.read_excel(uploaded_file, dtype={"Date": object})

a = df['Stocks'].unique()
a=sorted(a)
with st.sidebar:
    for item in a:
        st.write(item)



ticker = st.text_input('Stock Name')

if ticker != None:
    st.write(ticker)
    df3 = df.query('Stocks == @ticker')
    st.dataframe(df3)
