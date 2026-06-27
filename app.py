from flask import Flask, render_template, request
from speech_to_text import transcribe_audio
from minutes_generator import generate_minutes

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    audio = request.files['audio']
    audio.save(audio.filename)

    text = transcribe_audio(audio.filename)
    minutes = generate_minutes(text)

    return render_template(
        'result.html',
        transcription=text,
        minutes=minutes
    )

if __name__ == '__main__':
    app.run(debug=True)
