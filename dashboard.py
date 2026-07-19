import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import os

CSV_FILE = "emotion_log.csv"


def show_dashboard():

    st.header("📊 Emotion Analytics Dashboard")

    if not os.path.exists(CSV_FILE):
        st.info("No emotion history found.")
        return

    df = pd.read_csv(CSV_FILE)

    if df.empty:
        st.info("No emotion records available.")
        return

    st.subheader("Recent Emotion History")

    st.dataframe(df, use_container_width=True)

    st.subheader("Emotion Distribution")

    emotion_counts = df["Emotion"].value_counts()

    fig, ax = plt.subplots(figsize=(9, 5))

    emotion_counts.plot(
        kind="bar",
        ax=ax,
        color=[
            "#4CAF50",  # Green
            "#FFC107",  # Yellow
            "#2196F3",  # Blue
            "#F44336",  # Red
            "#9C27B0",  # Purple
            "#607D8B"   # Grey
        ]
    )

    ax.set_xlabel("Emotion")
    ax.set_ylabel("Number of Records")
    ax.set_title("Student Emotion Analysis")
    ax.grid(axis="y", linestyle="--", alpha=0.4)

    plt.xticks(rotation=0)

    st.pyplot(fig)

    st.subheader("📈 Statistics")

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