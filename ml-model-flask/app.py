from flask import Flask, request, jsonify
import joblib
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS so Spring Boot can call it

# Load the model
model = joblib.load('model.pkl')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    text = data.get('text', '')
    
    if not text.strip():
        return "Empty input", 400

    prediction = model.predict([text])[0]
    label = "SPAM" if prediction == 1 else "HAM"
    return label

if __name__ == '__main__':
    app.run(port=5500)
