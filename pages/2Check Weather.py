import streamlit as st
import requests
import datetime
from plotly import graph_objects as go
st.title("8-DAY WEATHER FORECAST 🌧️🌥️")

city=st.text_input("ENTER THE NAME OF THE CITY ")
state=option = st.selectbox(
    'State',
    ('Andhra Pradesh', 'Arunachal Pradesh', 'Assam', 'Bihar', 'Chhattisgarh', 'Goa', 'Gujarat', 
    'Haryana', 'Himachal Pradesh', 'Jharkhand', 'Karnataka', 'Kerala', 'Madhya Pradesh', 'Maharashtra', 
    'Manipur', 'Meghalaya', 'Mizoram', 'Nagaland', 'Odisha', 'Punjab', 'Rajasthan', 'Sikkim', 'Tamil Nadu', 
    'Telangana', 'Tripura', 'Uttar Pradesh', 'Uttarakhand', 'West Bengal', 'Andaman and Nicobar Islands', 
    'Chandigarh', 'Dadra and Nagar Haveli and Daman and Diu', 'Delhi', 'Lakshadweep', 'Puducherry'))


temp_unit=" °C"
wind_unit=" km/h"

# api="9c902441f6421a5c0178d29ef5d49a6a"
# url=f"http://api.openweathermap.org/geo/1.0/direct?q={city,state}&limit=1&appid={api}"
api="9b833c0ea6426b70902aa7a4b1da285c"
url=f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api}"
response=requests.get(url)
x=response.json()
if(st.button("SUBMIT")):
    try:
        # lon=x[0]["lon"]
        # lat=x[0]["lat"]
        # ex="current,minutely,hourly"
        # url2=f'https://api.openweathermap.org/data/3.0/onecall?lat={lat}&lon={lon}&exclude={ex}&appid={api}'
        # res=requests.get(url2)
        # y=res.json()
        lon=x["coord"]["lon"]
        lat=x["coord"]["lat"]
        ex="current,minutely,hourly"
        url2=f'https://api.openweathermap.org/data/2.5/onecall?lat={lat}&lon={lon}&exclude={ex}&appid={api}'
        res=requests.get(url2)
        y=res.json()

        maxtemp=[]
        mintemp=[]
        pres=[]
        wspeed=[]
        desc=[]
        cloud=[]
        rain=[]
        dates=[]
        cel=273.15
        
        for item in y["daily"]:
            maxtemp.append(round(item["temp"]["max"]-cel,2))
            mintemp.append(round(item["temp"]["min"]-cel,2))
            wspeed.append(str(round(item["wind_speed"],1))+wind_unit)
            

            pres.append(item["pressure"])
            
            cloud.append(str(item["clouds"])+' %')
            rain.append(str(int(item["pop"]*100))+'%')

            desc.append(item["weather"][0]["description"].title())

            d1=datetime.date.fromtimestamp(item["dt"])
            dates.append(d1.strftime('%d %b'))
    
            
        icon=x["weather"][0]["icon"]
        current_weather=x["weather"][0]["description"].title()
        weather_id=x["weather"][0]["id"]
        
        temp=str(round(x["main"]["temp"]-cel,2))
        
        col1, col2 = st.columns(2)
        with col1:
            st.write("## Current Temperature ")
        with col2:
            st.image(f"http://openweathermap.org/img/wn/{icon}@2x.png",width=70)

        
        col1, col2= st.columns(2)
        col1.metric("TEMPERATURE",temp+temp_unit)
        col2.metric("WEATHER",current_weather)
        st.subheader(" ")

         
        table1=go.Figure(data=[go.Table(header=dict(
                  values = [
                  '<b>DATES</b>',
                  '<b>MAX TEMP<br>(in'+temp_unit+')</b>',
                  '<b>MIN TEMP<br>(in'+temp_unit+')</b>',
                  '<b>CHANCES OF RAIN</b>',
                  '<b>CLOUD COVERAGE</b>',
                ],
                  line_color='black', fill_color='royalblue',  font=dict(color='white', size=14),height=32),
        cells=dict(values=[dates,maxtemp,mintemp,rain,cloud],
        line_color='black',fill_color=['paleturquoise',['palegreen', '#fdbe72']*7], font_size=14,height=32
            ))])

        table1.update_layout(margin=dict(l=10,r=10,b=10,t=10),height=328)
        st.write(table1)
        
        table2=go.Figure(data=[go.Table(columnwidth=[1,2,1,1,1,1],header=dict(values=['<b>DATES</b>','<b>WEATHER CONDITION</b>','<b>WIND SPEED</b>','<b>PRESSURE<br>(in hPa)</b>']
                  ,line_color='black', fill_color='royalblue',  font=dict(color='white', size=14),height=36),
        cells=dict(values=[dates,desc,wspeed,pres,],
        line_color='black',fill_color=['paleturquoise',['palegreen', '#fdbe72']*7], font_size=14,height=36))])
        
        table2.update_layout(margin=dict(l=10,r=10,b=10,t=10),height=360)
        st.write(table2)
        
        st.header(' ')
        st.header(' ')
        st.markdown(
                       """
                        <style>
                            .appview-container{
                                background-image: url(https://cdn.pixabay.com/photo/2015/07/05/10/18/tree-832079_1280.jpg);
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
    except KeyError:
        st.error(" Invalid city!!  Please try again !!")


