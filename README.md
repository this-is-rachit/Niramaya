# Nirāmaya-AI Project

## Table of Contents
1. [Project Overview](#project-overview)
2. [Features](#features)
3. [Technologies Used](#technologies-used)
4. [Installation](#installation)
5. [Usage](#usage)
6. [Acknowledgements](#acknowledgements)

## Project Overview
Nirāmaya is a web application designed to provide users with personalized guidance on drug interactions, leveraging the power of natural language generation and text-to-speech technology. The application aims to enhance medication safety by decoding and defusing potential drug interactions.

## Features
- **Drug Interaction Check**: Analyze and identify potential interactions between medications.
- **Personalized Guidance**: Tailored health advice based on user-provided health history and personal details.
- **Audio Support**: Converts the generated response to speech for easy accessibility.
- **User-friendly Interface**: Intuitive UI with custom styling for a better user experience.

## Technologies Used
- **Streamlit**: For building the web interface.
- **Google Generative AI**: For generating personalized drug interaction reports.
- **gTTS (Google Text-to-Speech)**: For converting text responses to speech.
- **Base64**: For encoding audio files.

## Installation
1. Clone the repository to your local machine:
   ```bash
   git clone https://github.com/this-is-rachit/Niramaya.git
   ```
2. Navigate to the project directory:
   ```bash
   cd Niramaya
   ```
3. Install the required Python packages:
   ```bash
   pip install streamlit google-generativeai gtts
   ```
4. Set up the environment variable for the API key:
    ```bash
   export GEMINI_API_KEY="your_api_key_here"
   ```
    
## Usage
1. Start the Streamlit application:
   ```bash
   streamlit run app.py
   ```
2. Open your web browser and navigate to the URL provided by Streamlit.
3. Enter the names of the medications you are currently taking in the provided text area.
4. Provide your health history and any relevant personal details (gender, age, weight, height) for personalized advice.
5. Click the Check Interactions button to analyze potential drug interactions and receive guidance.
6. Listen to the audio response and read the detailed explanation provided.

## Acknowledgements
>Inspired by the need for safer medication management and personalized health guidance.
>Icons and images are sourced from various online resources and are used for educational purposes.

