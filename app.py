from flask import Flask, jsonify
import socket
import datetime
import os

app = Flask(__name__)

APP_VERSION = os.environ.get("APP_VERSION", "1.0")

@app.route("/")
def home():
    return jsonify({
        "message": "Welcome to Production test Flask App testing app",
        "version": APP_VERSION,
        "hostname": socket.gethostname(),
        "timestamp": datetime.datetime.utcnow().isoformat()
    })

@app.route("/health")
def health():
    return jsonify({"status": "healthy"}), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

