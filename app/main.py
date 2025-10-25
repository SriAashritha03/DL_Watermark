from flask import Flask, request, jsonify
from app.model_loader import load_all_models
from app.inference import run_inference

app = Flask(__name__)
models = load_all_models()

@app.route('/predict', methods=['POST'])
def predict():
    input_data = request.json
    result = run_inference(models, input_data)
    return jsonify(result)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)