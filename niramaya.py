import streamlit as st
import google.generativeai as genai
from gtts import gTTS
import base64
import os

os.environ['GEMINI_API_KEY'] = "AIzaSyDxeK8aHA_ougElR10zEHizpsKh3eKTaUg"
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# UI configurations
st.set_page_config(page_title="Nirāmaya", page_icon='img/meditation.png')
custom_css = """
<style>
    h1 {
        font-size: 24px;
        color: #A7D3A9;
        padding: 0px 0px 40px 0px;
    }
    .stButton > button {
        background-color: #A7D3A9;
        color: #ffffff;
    }
    .stButton > button:hover {
        background-color: white;
        color: #A7D3A9;
    }
</style>
"""
st.markdown(custom_css, unsafe_allow_html=True)
st.image('img/banner.png', use_column_width=True)
st.title('Nirāmaya: Your prescription for peace of mind, empowering you to decode and defuse drug interactions, ensuring your safety with every prescription!')
st.write('Welcome to Nirāmaya! Uncover potential drug interactions and receive personalised guidance with our built-in audio support. Share your details below to embark on a safer health journey.')

# Compulsory field for medications
medications = st.text_area('Enter the names of the medications you are currently taking, separated by commas:', help='Please enter the names of the medications you are currently taking, separated by commas.')
health_history = st.text_area('Enter your health history or describe any ailments:', help='Please include any chronic conditions, recent illnesses, or relevant health issues.')

# Optional fields for personalized advice
options = ['Male', 'Female']
gender = st.selectbox('Choose your gender:', options)
age = st.text_input('Enter your age (Optional):', '')
weight = st.text_input('Enter your weight in kg (Optional):', '')
height = st.text_input('Enter your height in cm (Optional):', '')

# Function to check drug interactions
def check_drug_interactions(medications, health_history, gender="", age="", weight="", height=""):
    try:
        model = genai.GenerativeModel('gemini-pro')
        response = model.generate_content(
            "You are a knowledgeable assistant trained to provide information on drug interactions, but first classify the risk of interaction only into (Severe, Mild, Moderate) and then offer tailored health advice taking into account the patient's health history and personal details."
            f"Given the health history: {health_history}, provide a detailed explanation of the potential risks and interactions among these medications: {medications}."
            f"Focus on any increased risks, specific side effects, and the mechanism by which"
            f"these interactions might occur, also considering the health history. Include any relevant studies or findings that have implicated these drugs in such conditions. "
            f"Ensure the explanation is comprehensive, covering the pharmacological aspects and clinical implications for patients. "
            f"Then, based on gender: {gender}, age: {age}, weight: {weight}, height: {height}, and health history {health_history}, offer tailored advice."       
        )
        return response.text
    except Exception as e:
        return f"An error occurred: {str(e)}"

# Function to convert text to speech and return the audio file path
def text_to_speech(text):
    tts = gTTS(text)
    audio_path = 'response.mp3'
    tts.save(audio_path)
    return audio_path

# Button to initiate the drug interaction check
if st.button('Check Interactions'):
    warning_users = "<p style='color: #BABABA; opacity:.7;'>  Thank you for choosing Nirāmaya for your medication management needs. Please remember that Nirāmaya is intended to complement, not replace, professional medical advice. For personalized health recommendations, always consult with your doctor or healthcare provider.  </p>" 
    st.markdown(warning_users, unsafe_allow_html=True)
    if medications and health_history:
        response = check_drug_interactions(medications, health_history, gender, age, weight, height)         
        # Convert the response to speech
        audio_file_path = text_to_speech(response)
        
        # Read the audio file and encode it to base64
        with open(audio_file_path, "rb") as audio_file:
            audio_bytes = audio_file.read()
            encoded_audio = base64.b64encode(audio_bytes).decode()
            audio_html = f'<audio controls autoplay><source src="data:audio/mpeg;base64,{encoded_audio}" type="audio/mpeg"></audio>'
            st.markdown(audio_html, unsafe_allow_html=True)

        st.write('**Response:**', response)
       
    else:
        st.warning('Please enter the required information to continue.')

# Footer
footer = """<style>
a:link , a:visited{
color: #BADEDC;
background-color: transparent;
text-decoration: underline;
}

a:hover,  a:active {
color: #A7D3A9;
background-color: transparent;
text-decoration: underline;
}

.footer {
position: fixed;
left: 0;
bottom: 0;
width: 100%;
background-color: transparent;
color: #64928F;
text-align: center;
}
</style>
<div class="footer">
<p>  <a>Thank you for choosing Nirāmaya—your trusted partner in navigating the world of medications!</a> <a style='display: block; text-align: center;' href="https://drive.google.com/file/d/1ahasDbmSfbY9ysTyoMuwTjARaS2gJtpl/view?usp=sharing" target="_blank">About Nirāmaya</a></p>
</div>
"""
st.markdown(footer, unsafe_allow_html=True)
