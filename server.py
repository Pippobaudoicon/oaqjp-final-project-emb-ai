'''
This module provides a Flask web server for emotion detection.
'''

from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

def _is_blank_response(response_data):
    '''Checks if the emotion detector response indicates a blank input.

    Args:
        response_data (dict): The response from the emotion_detector.

    Returns:
        bool: True if all emotion scores are None, False otherwise.
    '''
    if response_data is None:
        return False # Or handle as an error, but current logic implies it won't be None here
    return (
        response_data.get('anger') is None and
        response_data.get('disgust') is None and
        response_data.get('fear') is None and
        response_data.get('joy') is None and
        response_data.get('sadness') is None
    )

@app.route("/")
def render_index_page():
    '''Renders the index.html page.

    This function is called when the user navigates to the root URL.
    '''
    return render_template('index.html')

@app.route("/emotionDetector")
def detect_emotion():
    '''Receives text from the client, analyzes emotion, and returns a formatted string.

    This function is called when the user submits text for emotion analysis.
    It expects a 'textToAnalyze' query parameter.
    '''
    text_to_analyze = request.args.get('textToAnalyze')
    if not text_to_analyze:
        return "Error: No text provided for analysis.", 400

    response = emotion_detector(text_to_analyze)

    if response is None or response.get('dominant_emotion') is None:
        if _is_blank_response(response):
            return "Invalid text! Please try again!"
        return "Error: Could not analyze emotion. Please check the input or server logs.", 500

    anger_score = response.get('anger', 0.0)
    disgust_score = response.get('disgust', 0.0)
    fear_score = response.get('fear', 0.0)
    joy_score = response.get('joy', 0.0)
    sadness_score = response.get('sadness', 0.0)
    dominant_emotion = response.get('dominant_emotion')

    output_string = (
        f"For the given statement, the system response is 'anger': {anger_score}, "
        f"'disgust': {disgust_score}, 'fear': {fear_score}, 'joy': {joy_score} and "
        f"'sadness': {sadness_score}. The dominant emotion is {dominant_emotion}."
    )
    return output_string

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
