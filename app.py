import streamlit as st
import pandas as pd
# df = pd.DataFrame({
#   'first column': [1, 2, 3, 4],
#   'second column': [10, 20, 30, 40]
# })

# df

if 'stdt' not in st.session_state:
    st.session_state['stdt'] = 0

if 'eddt' not in st.session_state:
    st.session_state['eddt'] = 0


uploaded_file = st.file_uploader('Upload xlsx file')
df=pd.read_excel(uploaded_file, dtype={"Date": object})

# return the dtype of each column
result = df.dtypes

# Print the result
# st.write(result)

df['Date'] = pd.to_datetime(df['Date'], format="%Y-%m-%d")
# df.reset_index(inplace=True)
# df = df.set_index(['Date'])

st.dataframe(df)

# return the dtype of each column
result = df.dtypes

# Print the result
# st.write(result)



# df['Date'] = pd.to_datetime(df['Date']).dt.date
# df.index = pd.to_datetime(df.index)

# return the dtype of each column
# result = df.dtypes

# # Print the result
# st.write(result)

col1, col2, col3 = st.columns(3)

    

st.write(st.session_state['stdt'])
# if st.session_state['stdt'] != 0 & st.session_state['eddt'] != 0:
#     st.write('set')
#     df2=df.loc[stdt:eddt]
#     st.dataframe(df2)
# else:
#     st.write('x')    


def form_callback():
    st.write(stdt)
    st.write(eddt)

    df2 = df.query('Date >= @stdt and Date <= @eddt')
    # df2=df.loc[stdt:eddt]
    st.dataframe(df2)

with st.form(key='my_form'):
    stdt=st.date_input ('start date',value=None , min_value=None , max_value=None , key=None )
    eddt=st.date_input ('end date',value=None , min_value=None , max_value=None , key=None )
    submit_button = st.form_submit_button(label='Submit', on_click=form_callback)
