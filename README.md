#  AI Mood Predictor 

A lightweight machine learning application that predicts your mood score (1–10) based on daily habits like **sleep duration, screen time, and exercise**.

Built using **Scikit-learn**, **Python**, and deployed with **Gradio**.

##  Overview

This project is designed to help users understand how their daily routine affects their mental well-being. It predicts your mood and provides a short motivational message.

This is a **beginner-friendly ML project** demonstrating:

* Data preprocessing
* Training a regression model
* Saving/loading models (`joblib`)
* Deploying an ML app

---

##  Features

* **Predicts mood score** on a scale of 1–10.
* Provides contextual **motivational messages**.
* Clean & simple **Gradio Web UI**.
* Fully deployable on **Hugging Face Spaces**.
* Model saved as `mood_model.pkl`.

---

## Project Structure

ai_mood_predictor/ │ ├── app.py # Gradio app logic ├── mood_model.pkl # Saved ML model (Linear Regression) ├── requirements.txt # Python dependencies └── README.md # Documentation


---

##  Machine Learning Model

The model used is **Linear Regression**.

### Training Pipeline:

1.  Collect habit data.
2.  Train/Validation split.
3.  Train Linear Regression model.
4.  Save model using `joblib.dump()`.
5.  Load model inside `app.py` for predictions.

---

##  Inputs & Output

### Input fields

* Sleep Hours
* Screen Time (hours)
* Exercise Time (minutes)

### Output

* Mood Score (1–10)
* Motivational message (e.g., Excellent Mood 😄, Low Mood 😟)

---

## 🖥 Demo (Hugging Face Space)

https://huggingface.co/spaces/devu-197/mood_predictor

---



**Tech Stack**

Python

Scikit-learn

NumPy / Pandas

Joblib

Gradio

Hugging Face Spaces

**Future Improvements**

Add more lifestyle inputs.

Use a Neural Network for better prediction.

Store user mood history.

Add charts & visual analytics.

Mobile app integration.

 **Author**
 
Devu Suresh AI & Web Development Beginner | Building practical ML projects
