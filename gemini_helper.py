import os
from dotenv import load_dotenv
import google.generativeai as genai

# Load API key from .env
load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Gemini model
model = genai.GenerativeModel("gemini-2.0-flash")


def get_learning_support(user_text, emotion):
    prompt = f"""
You are a helpful AI tutor.

Student Emotion: {emotion}

Student Message:
{user_text}

Give:
1. Emotional support.
2. Study advice.
3. Motivation.

Keep the response under 100 words.
"""

    try:
        response = model.generate_content(prompt)
        return response.text

    except Exception:

        if emotion == "Confident":
            return (
                "Great work! Your confidence shows you're making progress. "
                "Continue solving more challenging problems and keep practicing regularly."
            )

        elif emotion == "Confused":
            return (
                "Don't worry. Review the topic step by step, practice simple examples, "
                "and ask questions whenever you get stuck."
            )

        elif emotion == "Curious":
            return (
                "Your curiosity is your greatest strength. Explore additional resources, "
                "watch tutorials, and try building small projects to deepen your understanding."
            )

        elif emotion == "Frustrated":
            return (
                "Take a short break and come back with a fresh mind. "
                "Focus on one concept at a time and don't hesitate to seek help."
            )

        elif emotion == "Bored":
            return (
                "Try a different learning method such as videos, coding exercises, "
                "or interactive quizzes to make studying more engaging."
            )

        else:
            return (
                "Keep learning consistently. Every small step helps you improve."
            )