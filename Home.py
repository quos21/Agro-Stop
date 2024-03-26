import streamlit as st

st.set_page_config(
    page_title="Agro-Stop",
    page_icon="👨🏽",
)

st.write("# Welcome👨🏽")

name=st.text_input('Enter your name')



if name:
    st.markdown(
        f'''
        ## Hi {name} how can I assist you?
        - ##### If you have any query regarding your crop Ask our Bot(He will try his best)!

        - ##### Want to check the weather for the next 8 days? Check our weather forecast to stay updated!

        - ##### Want to get the market prices of a crop? Checkout our price list(Now bringing more prices very soon!!!!)


        '''
    )
st.markdown(
        """
        <style>
            .stApp{
                background-image: url(https://static.vecteezy.com/system/resources/previews/026/797/629/large_2x/farmer-s-hands-over-farm-plants-realistic-image-ultra-hd-high-design-very-detailed-free-photo.jpg);
                height: 950px; /* You must set a specified height */
                background-repeat: no-repeat; /* Do not repeat the image */
                background-size: cover;
            }
            .st-emotion-cache-6qob1r.eczjsme3{
                background-color: grey;
                background-image: linear-gradient(to right, rgba(255,0,0,0), rgba(255,0,0,1));;
            }
        </style>
        """,
        unsafe_allow_html=True
    )
