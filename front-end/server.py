"""
Flask web application for sentiment analysis using Emotion Detection.
"""
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Sentiment Analyzer")

@app.route("/")
def render_index_page():
    """Renders the index.html page."""
    return render_template("index.html")

@app.route("/emotionDetector")
def sent_analyzer():
    """
    Analyzes the emotion of the given text.
    
    Returns:
        str: Analysis result including emotion scores and dominant emotion.
    """
    text_to_analyze = request.args.get("textToAnalyze")
    
    response = emotion_detector(text_to_analyze)
    anger = response["anger"]
    disgust = response["disgust"]
    fear = response["fear"]
    joy = response["joy"]
    sadness = response["sadness"]
    dominant_emotion = response["dominant_emotion"]

    if any(value is None for value in (anger, disgust, fear, joy, sadness)):
        return "Invalid input! Try again."

    return (
        f"For the given statement, the system response is 'anger': {anger}, "
        f"'disgust': {disgust}, 'fear': {fear}, 'joy': {joy}, and 'sadness': {sadness}. "
        f"The dominant emotion is {dominant_emotion}."
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)