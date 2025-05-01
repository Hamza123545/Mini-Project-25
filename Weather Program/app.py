import streamlit as st
import requests


def get_weather(city):
    api_key = 'your_api_key' 
    base_url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
    response = requests.get(base_url)
    return response.json()


st.title('Weather App')
city = st.text_input('Enter a city:')
if city:
    data = get_weather(city)
    if data['cod'] == 200:
        st.write(f"Weather in {city}: {data['weather'][0]['description']}")
        st.write(f"Temperature: {data['main']['temp']}°K")
    else:
        st.write("City not found!")
