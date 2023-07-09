import streamlit as st
import webbrowser
from st_pages import Page, add_page_title, show_pages
from PIL import Image

show_pages(
    [
        Page("website.py", "About Me", "👩"),
        Page("experience.py", "My Experience", "📜"),
    ]
)

col1, col2 = st.columns(2)

with col1:
   st.title('Vidhi Patra')
with col2:
    image1 = Image.open('Vidhi Patra.jpg')
    st.image(image1, width=150)


url = 'https://github.com/vidhip222'
if st.button('Github'):
    webbrowser.open_new_tab(url)


st.header('About Me')
st.markdown("""
Hi, my name is Vidhi Patra. I'm a high schooler based in the 
Bay Area with a deep passion for artificial intelligence, 
machine learning, and data science! From an early age, I've 
always been fascinated by the possibilities and potential of AI 
technology. I love how it can simulate human intelligence and 
solve complex problems. I like to learn by doing projects, and 
I have numerous on my GitHub profile. """)

st.markdown("""
**School:** Milpitas High School """)

st.markdown("""
**Class:** 2024 """)

st.markdown("""
**Grade:** 12 """)

st.markdown("""
**Email:** mailtovidhipatra@gmail.com""")


st.caption("Made by **Vidhi Patra**")

# command:

# cd desktop/VidhiHACK/personal_website/vidhip222.github.io
# streamlit run website.py