import streamlit as st
import webbrowser
from st_pages import Page, add_page_title, show_pages
from PIL import Image


show_pages(
    [
        Page("website.py", "About Me", "📈"),
        Page("experience.py", "My Experience", "💵"),
    ]
)


st.header('Internships:')
st.markdown("""
* Lorven- Coding intern at a startup. I built an employment management system using Python.
* Building U- Coding intern at a nonprofit. Contributed in building a game to help high schoolers earn scholarship money.
* Boldly Me- Business intern at a nonprofit. I helped raised $12,000 in funding for a marathon to raise awareness for mental health
""")


st.header('Programs:')
st.markdown("""
* MIT BeaverWorks- (in progress) I am part of the Disaster Response team.
* UC Santa Cruz Science Internship Program- (in progress) I am part of the Applied Artificial Intelligence (AAI 1) group.
* Girls Who Code Summer Immersion Program- Built multiple interactive games using JavaScript.
* UC Berkeley Society of Women Engineering High School Engineering Program- Built the hardware and software for a smart thermostat and 
humidity detector for preventing house fires.
""")


st.header('Activities:')
st.markdown("""
* Ambassador in Girl Scouts- I raised awareness about energy efficiency to 500+ citizens, created a math YouTube channel with 200+ views 
on each video, and conducted drives to raise 50+ coats, 100+ cards, wool hats, and masks for Washington Hospital.
* Speech and Debate- I primarily do Lincoln Douglas and Parliamentary style debate. I also do exempt and oratorical interpretation style 
speech.
* Tutor- I tutor students from Algebra to Calculus, Spanish 1 to Spanish 3, and in different programming languages.
* Exhibit Interpreter at Tech Museum- I explain the exhibits at the Tech Museum to the visitors. Some exhibitions include cyber security,
 A.I. detecting Lego animals, bacteria labs, and more.
* Author- As of now, I have wriiten 10 articles about different topics in AI. 
""")


st.header('Clubs:')
st.markdown("""
* Code4Good- I am currently serving as the president of this club. Through this club, I hosted my school's first-ever hackathon and had 
100+ participants. I also organized other social benefitting projects and increased the membership of female club members and officers 
significantly by creating a more inclusive and collaborative environment.
* Decode CS- I am currently serving as the president of this club. Through this club, I primarily taught 100+ students in my school 
and the local libraries about various CS topics. 
""")


st.header('Community College Courses:')
st.markdown("""
* Python 
* Artificial Intelligence and Data Science 
* US History  
* American Government 
""")


st.header('Projects:')
st.write('*only includes some projects')

st.subheader('ProfitPal')
st.write('Detects stock prices based on financial tweets, displays stock prices, and hosts an interactive data table of S&P 500 stocks.')
st.write('Techniques: Logistic Regression, Long Short-Term Memory (LSTM), Bidirectional Encoder Representations from Transformers (BERT) and' 
         'other NLP techniques')
st.write('Data: 2037 Training Tweets and 227 Testing Tweets')
#see presentation

st.subheader('A.I. Facial Emotion Detector')
st.write('A game for children with autism who have a hard time detecting facial emotions. This game helps the player determine how close' 
         'they are to the actual emotions, and the player receives a special prize if they are correct.')
st.write('Techniques: Cascade Classifier, Adam Optimizer, and other Computer Vision techniques')
st.write('Data: 28709 Training Face Pictures and 7178 Testing Face Pictures')
#see this website: https://www.inspiritai.com/blogs/ai-blog/2021/8/28/student-blog-project-bridging-ai-and-facial-recognition

st.subheader('Sale Stalker')
st.write('Detects prices of items on Amazon.')
st.write('Techniques: Web Scrapping, HTML Parsing, and more')

st.subheader('Melody Global')
st.write('Recommends a personalized playlist from songs around the world based on the Spotify history of the user.')

st.subheader('Carbon Calculator')
st.write('Calculates carbon footprint based on user inputs.')

st.subheader('All About the NBAs')
st.write('Displays NBA players stats.')
st.write('Techniques: Web Scrapping, HTML Parsing, and more')

st.subheader('K-12 Educational Website')
st.write('An AR animal identification game for elementary schoolers, a calculator for middle schoolers,' 
         'and a summarizer for high schoolers.')

st.subheader('Fake News Detector')
st.write('This model decides whether the news website is fake or real.')
st.write('Techniques: Web Scrapping and ML')
st.write('Data: 538 Training and 61 Testing')

st.subheader('Handwriting Detector')
st.write('Used the MNIST dataset to idenify handwriting. ')
st.write('Techniques: CNN')
st.write('Data: 60,000 Training and 10,000 Testing')

st.header('Awards:')
st.markdown("""
* Maroon Cord- I accumulated 300+ hours of community service. 
* Girl Scout Gold Award- For my efforts in raising awareness and funds for school clubs by creating websites for them to 
connect with the student body and local businesses.
* Hackathon Winner for ProfitPal and Facial Emotion Detector. 
* Multiple Speech and Debate awards. 
* AP Scholar
""")

st.header('Computer Skills:')
st.markdown("""
* Python
* Java
* HTML
* CSS
* JavaScript
* Jupyter Notebook
* Streamlit
* Bootstrap
* Scratch
* Arduino
* and more!
""")




st.caption("Made by **Vidhi Patra**")
