from flask import Flask, request, jsonify, render_template
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/emotionDetector', methods=['GET', 'POST'])
def emotion_detector_api():
    if request.method == 'POST':
        data = request.json
        text_to_analyze = data.get('text', '')
    else:  # Handle GET request
        text_to_analyze = request.args.get('textToAnalyze', '')

    result = emotion_detector(text_to_analyze)

    if result['dominant_emotion'] is None:  # Handle the case where the input text is invalid
        return "Invalid text! Please try again!"

    # Format the response string
    response_text = (
        f"For the given statement, the system response is 'anger': {result['anger']}, "
        f"'disgust': {result['disgust']}, 'fear': {result['fear']}, "
        f"'joy': {result['joy']} and 'sadness': {result['sadness']}. "
        f"The dominant emotion is {result['dominant_emotion']}."
    )

    return response_text

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
