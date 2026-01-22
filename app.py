from flask import Flask, jsonify
import random

app = Flask(__name__)

quotes = [
    "Keep it simple.",
    "First, solve the problem.",
    "Stay curious!",
    "Hello from Kubernetes! 🚀"
]

@app.route("/")
def home():
    return jsonify({"message": "Welcome!", "quote": random.choice(quotes)})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
    
    
    
# docker tag my-python-k8s-app:latest faruk67/my-python-k8s-app:latest
# docker push faruk67/my-python-k8s-app:latest
# http://192.168.49.2/

