@app.route("/ask", methods=["POST"])
def ask():
    user_input = request.json["message"]

    # 🔥 ADD THIS HERE
from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import openai

app = Flask(__name__)
CORS(app)

import os
openai.api_key = os.getenv("OPENAI_API_KEY")

# 👇 ADD THIS
@app.route("/")
def home():
    return render_template("index.html")
    import os
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 10000)))