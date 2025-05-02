import streamlit as st
import datetime
import matplotlib.pyplot as plt

def log_mood(mood_log, mood_value):
    mood_log.append((datetime.datetime.now(), mood_value))
    st.success("Mood logged!")

def show_mood_chart(mood_log):
    if mood_log:
        times, moods = zip(*mood_log)
        fig, ax = plt.subplots()
        ax.plot(times, moods, marker="o", linestyle="--", color="purple")
        ax.set_title("Mood Over Time")
        ax.set_xlabel("Time")
        ax.set_ylabel("Mood (1–10)")
        st.pyplot(fig)
