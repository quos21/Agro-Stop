import streamlit as st
import pandas as pd

@st.cache_data
def table(file):
    df=pd.read_csv(file)
    return df
try:
    crop=st.text_input('Write the name of the crop')
    df=table('final2.csv')
    crops=crop.upper()
    filtered_df = df[df['Commodity'] == crops]
    if not filtered_df.empty:
        st.dataframe(filtered_df.style.set_properties(**{'background-color': 'lightblue', 'color': 'black', 'font-size': '16px'}))
except KeyError:
    st.error('Please enter a valid value.')
except NameError:
    st.error('Reopen the link/ Reload the page')
st.markdown(
        """
        <style>
            .st-emotion-cache-6qob1r.eczjsme3{
                background-color: grey;
                background-image: linear-gradient(to right, rgba(255,0,0,0), rgba(255,0,0,1));;
            }
        </style>
        """,
        unsafe_allow_html=True
)
