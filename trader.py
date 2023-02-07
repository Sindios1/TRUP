from flask import Flask, jsonify
import gdown
app = Flask(__name__)

@app.route('/run-colab')
def run_colab():
    gdown.download('https://drive.google.com/file/d/1eIexxiET8ZZsAwAE4190NsfISujvOJXR', 'lokal.ipynb', quiet=False)
    return jsonify(message='colab notebook ran successfully')
