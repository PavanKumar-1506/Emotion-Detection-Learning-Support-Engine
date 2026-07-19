import streamlit as st
import csv
import os
from datetime import datetime
import pandas as pd
import matplotlib.pyplot as plt

from emotion_detector import detect_emotion
from support import support_messages
from dashboard import show_dashboard
from gemini_helper import get_learning_support


# -----------------------------
# Streamlit Page Configuration
# -----------------------------
st.set_page_config(
    page_title="Emotion Detection & Learning Support Engine",
    page_icon="😊",
    layout="wide"
)

st.title("😊 Emotion Detection & Learning Support Engine")

st.markdown("""
### Welcome!

This AI-powered application detects a student's emotional state
from text input and provides personalized learning support using Gemini AI.

**Supported Emotions**

- 😊 Confident
- 😕 Confused
- 😃 Curious
- 😞 Frustrated
- 😴 Bored
""")


# -----------------------------
# CSV File
# -----------------------------
CSV_FILE = "emotion_log.csv"


# -----------------------------
# Save Emotion History
# -----------------------------
def save_emotion_log(user_text, emotion):

    file_exists = os.path.isfile(CSV_FILE)

    with open(CSV_FILE, "a", newline="", encoding="utf-8") as file:

        writer = csv.writer(file)

        if not file_exists:

            writer.writerow([
                "Date",
                "User Input",
                "Emotion"
            ])

        writer.writerow([
            datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            user_text,
            emotion
        ])


# -----------------------------
# Sidebar
# -----------------------------
st.sidebar.title("Navigation")

page = st.sidebar.radio(
    "Select Page",
    [
        "Emotion Detection",
        "Dashboard"
    ]
)
# ---------------------------------------
# Emotion Detection Page
# ---------------------------------------

if page == "Emotion Detection":

    st.header("Student Emotion Analysis")

    user_input = st.text_area(
        "Enter how you're feeling while studying:",
        height=180,
        placeholder="Example: I am confused about Python loops and feeling frustrated..."
    )

    if st.button("Analyze Emotion"):

        if user_input.strip() == "":

            st.warning("Please enter some text.")

        else:

            # Detect emotion
            emotion = detect_emotion(user_input)

            # Save history
            save_emotion_log(user_input, emotion)

            st.subheader("Detected Emotion")

            if emotion == "Confident":
                st.success("😊 Confident")

            elif emotion == "Confused":
                st.warning("😕 Confused")

            elif emotion == "Curious":
                st.info("😃 Curious")

            elif emotion == "Frustrated":
                st.error("😞 Frustrated")

            elif emotion == "Bored":
                st.warning("😴 Bored")

            else:
                st.info("😐 Neutral")

            st.divider()

            st.subheader("Learning Support")

            # Default support message
            if emotion in support_messages:
                st.info(support_messages[emotion])

            st.divider()

            st.subheader("Gemini AI Learning Assistant")

            with st.spinner("Generating AI guidance..."):

                try:

                    ai_response = get_learning_support(
                        user_input,
                        emotion
                    )

                    st.success(ai_response)

                except Exception as e:

                    st.error(f"Gemini Error: {e}")

            st.success("✅ Emotion saved successfully!")
            # ---------------------------------------
# Dashboard Page
# ---------------------------------------

elif page == "Dashboard":

    st.header("📊 Emotion Analytics Dashboard")

    if os.path.exists(CSV_FILE):

        try:

            df = pd.read_csv(CSV_FILE)

            if len(df) == 0:
                st.warning("No emotion history found.")

            else:

                st.subheader("Recent Emotion History")

                st.dataframe(df, use_container_width=True)

                st.subheader("Emotion Distribution")

                emotion_counts = df["Emotion"].value_counts()

                fig, ax = plt.subplots(figsize=(8, 5))

                emotion_counts.plot(
                    kind="bar",
                    ax=ax
                )

                ax.set_xlabel("Emotion")
                ax.set_ylabel("Count")
                ax.set_title("Student Emotion Analysis")

                st.pyplot(fig)

                st.subheader("Statistics")

                col1, col2 = st.columns(2)

                with col1:
                    st.metric(
                        "Total Records",
                        len(df)
                    )

                with col2:
                    st.metric(
                        "Most Common Emotion",
                        emotion_counts.idxmax()
                    )

        except Exception as e:

            st.error(f"Dashboard Error: {e}")

    else:

        st.info("No emotion history available yet.")


# ---------------------------------------
# Footer
# ---------------------------------------

st.markdown("---")

st.markdown(
    """
**Emotion Detection & Learning Support Engine**

Developed using:
- Streamlit
- Python
- Gemini AI
- Pandas
- Matplotlib
"""
)
            