import pandas as pd
import streamlit as st

# Load data
df = pd.read_csv('IOD_Schema_Total.csv', thousands=',')

# Data formatting
df['Value'] = pd.to_numeric(df['Value'], errors='coerce')
df['Time'] = df['Time'].astype(str)

st.title('Iran Microeconomy Indicators')

# Filtering 
indics = df['sub0'].unique().tolist()
select_indic = st.selectbox('Select Indicator', indics)
filtered_df = df[df['sub0'] == select_indic].reset_index(drop=True)

st.subheader(f'Iran {select_indic} Data')

col1, col2, col3 = st.columns(3)
with col1:
  if filtered_df['sub1'].nunique() > 1:
    sub1 = filtered_df['sub1'].unique().tolist()
    select_sub1 = st.selectbox('Select Subcategory', sub1)
    filtered_df = filtered_df[filtered_df['sub1'] == select_sub1].reset_index(drop=True)

with col2:
  if filtered_df['sub2'].nunique() > 1:
    sub2 = filtered_df['sub2'].unique().tolist()
    select_sub2 = st.selectbox('Select Subcategory', sub2)
    filtered_df = filtered_df[filtered_df['sub2'] == select_sub2].reset_index(drop=True)

with col3:  
  if filtered_df['sub3'].nunique() > 1:
    sub3 = filtered_df['sub3'].unique().tolist()
    select_sub3 = st.selectbox('Select Subcategory', sub3)
    filtered_df = filtered_df[filtered_df['sub3'] == select_sub3].reset_index(drop=True)


  if filtered_df['sub5'].nunique() > 1:
    source = filtered_df['sub5'].unique().tolist()  
    select_source = st.selectbox('Select Source', source)
    filtered_df = filtered_df[filtered_df['sub5'] == select_source].reset_index(drop=True)

  if filtered_df['sub6'].nunique() > 1:
    time = filtered_df['sub6'].unique().tolist()
    select_time = st.selectbox('Select Time', time)
    filtered_df = filtered_df[filtered_df['sub6'] == select_time].reset_index(drop=True)

  if filtered_df['sub7'].nunique() > 1:
    unit = filtered_df['sub7'].unique().tolist()
    select_unit = st.selectbox('Select Unit', unit)
    filtered_df = filtered_df[filtered_df['sub7'] == select_unit].reset_index(drop=True) 


# Display data
output = filtered_df[['Indicator','Source','Time','Value','Unit','Details']].reset_index(drop=True)
csv = output.to_csv(index=False).encode('utf-8')
st.download_button(
    label='Download Data as CSV',
    data= csv,
    file_name='Iran_GDP_Filtered_Data.csv',
    mime='text/csv'
)
st.dataframe(output)

# chart
if filtered_df['sub4'].nunique() >= 1:
    st.bar_chart(filtered_df.set_index('Indicator')['Value'])
else:
    st.line_chart(filtered_df.set_index('Time')['Value'])
    
