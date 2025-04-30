import streamlit as st
import requests
from bs4 import BeautifulSoup

st.title('Web Scraping Tool')

url = st.text_input('Enter URL to scrape:', '')

if url:
    
    try:
        response = requests.get(url)
        response.raise_for_status()  
    except requests.exceptions.RequestException as e:
        st.error(f"Error fetching the URL: {e}")
    else:
        soup = BeautifulSoup(response.text, 'html.parser')

        
        st.subheader('Page Title:')
        if soup.title:
            st.write(soup.title.string)
        else:
            st.write("No title tag found")

    
        st.subheader('Extracted Text:')
        paragraphs = soup.find_all('p')
        if paragraphs:
            for para in paragraphs:
                st.write(para.text)
        else:
            st.write("No paragraphs found on this page.")
