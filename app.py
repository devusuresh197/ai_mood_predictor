import gradio as gr
import joblib
import pandas as pd
import numpy as np

# Load model
model = joblib.load("mood_model.pkl")

# Convert score → message
def get_mood_message(score):
    if score >= 8:
        return f"{score}/10 😊 Excellent mood! Keep shining!"
    elif score >= 6:
        return f"{score}/10 🙂 Good mood! Stay positive!"
    elif score >= 4:
        return f"{score}/10 😐 Neutral mood. Try doing something you enjoy."
    elif score >= 2:
        return f"{score}/10 😞 Low mood. Take a break and relax."
    else:
        return f"{score}/10 😣 Very low mood. Be kind to yourself today."

# Prediction
def predict_mood(sleep_hours, screen_time, exercise_minutes):
    data = np.array([[sleep_hours, screen_time, exercise_minutes]])
    score = int(model.predict(data)[0])  
    message = get_mood_message(score)
    return message

# Gradio UI
demo = gr.Interface(
    fn=predict_mood,
    inputs=[
        gr.Number(label="Sleep Hours"),
        gr.Number(label="Screen Time (hours)"),
        gr.Number(label="Exercise (minutes)")
    ],
    outputs=gr.Textbox(label="Mood Score & Message"),
    title="AI Mood Predictor (Out of 10)",
)

demo.launch()