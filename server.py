"""
Server module for the emotion detection web application.

This module uses Flask to create a web server that accepts user input for emotion detection
and returns the detected emotions using the Watson NLP API.
"""

from flask import Flask, request, render_template  # Removed unused jsonify import
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

@app.route('/')
def home():
    """
    Render the home page.
    Returns:
        HTML template for the home page.
    """
    return render_template('index.html')


@app.route('/emotionDetector', methods=['GET', 'POST'])
def emotion_detector_api():
    """
    API endpoint to analyze emotions in the provided text.
    Handles both GET and POST requests.
    
    Returns:
        JSON or plain text response with the analyzed emotions.
    """
    if request.method == 'POST':
        data = request.json
        text_to_analyze = data.get('text', '')
    else:  # Handle GET request
        text_to_analyze = request.args.get('textToAnalyze', '')

    result = emotion_detector(text_to_analyze)

    if result['dominant_emotion'] is None:
        return "Invalid text! Please try again!"

    response_text = (
        f"For the given statement, the system response is 'anger': {result['anger']}, "
        f"'disgust': {result['disgust']}, 'fear': {result['fear']}, "
        f"'joy': {result['joy']} and 'sadness': {result['sadness']}. "
        f"The dominant emotion is {result['dominant_emotion']}."
    )

    return response_text


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
