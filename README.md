# Emotion Detection Learning Support Engine

## Project Overview

The Emotion Detection Learning Support Engine is an AI-based platform that detects learner emotions from text input and provides personalized learning support.

The system analyzes user text, classifies emotions, and generates supportive guidance to improve the learning experience.

## Features

- Emotion detection from learner text
- AI-based personalized support responses
- Gemini AI learning assistant
- Emotion tracking and logging
- Dashboard for analyzing emotion trends
- Streamlit-based interactive user interface
- Support for multiple emotion categories

## Emotion Categories

The system identifies:

- Bored
- Confident
- Confused
- Curious
- Frustrated

## Technologies Used

- Python
- Streamlit
- BERT
- BiLSTM
- Gemini API
- Natural Language Processing (NLP)
- Machine Learning
- Pandas
- Matplotlib

## Project Structure

```text
Emotion-Detection-Learning-Support-Engine

├── app.py                  - Main Streamlit application
├── dashboard.py            - Emotion visualization dashboard
├── emotion_detector.py     - Emotion classification logic
├── gemini_helper.py        - Gemini AI response generation
├── support.py              - Support response module
├── emotion_log.csv         - Stores detected emotion records
├── requirements.txt        - Required Python libraries
└── README.md               - Project documentation
```
## How to Run

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run the Application

```bash
streamlit run app.py
```

The application will open automatically in your browser.

## Working Flow

1. Student enters their learning difficulty or feeling while studying.
2. The system analyzes the text input.
3. The emotion is detected.
4. Gemini AI generates personalized learning support.
5. The emotion is saved for future analysis.

## Application Output

The application provides:

- Emotion detection from student text input
- Personalized learning support
- Gemini AI-generated guidance
- Emotion logging and tracking
- Interactive Streamlit interface

## Internship Project

Developed as part of the Skill Wallet internship project.
