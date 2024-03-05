"""
flask based server interface to provide emotiond detection functionalities
"""

from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detecor")

@app.route("/emotionDetector")
def sent_analyzer():
    """
    this function analyzes the input text
    """
    text_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyze)
    print(response)
    anger_score = response['anger_score']
    disgust_score = response['disgust_score']
    fear_score = response['fear_score']
    joy_score = response['joy_score']
    sadness_score = response['sadness_score']
    dominant_emotion = response['dominant_emotion']
    if dominant_emotion is None:
        return "Invalid text! Please try again!"
    beginning_phrase = "For the given statement, the system response is "
    anger = f"'anger': {anger_score}, "
    disgust = f"'disgust': {disgust_score}, "
    fear = f"'fear': {fear_score}, "
    joy = f"'joy': {joy_score} "
    sadness = f"and 'sadness': {sadness_score}. "
    final_phrase = f"The dominant emotion is {dominant_emotion}."
    return beginning_phrase + anger + disgust + fear + joy + sadness + final_phrase

@app.route("/")
def render_index_page():
    """
    renders the main page
    """
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=6000)
