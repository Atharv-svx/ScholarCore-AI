from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import openai
import os

# ✅ CREATE app FIRST
app = Flask(__name__)
CORS(app)

# ✅ API Key
openai.api_key = os.getenv("OPENAI_API_KEY")

# ✅ Home route
@app.route("/")
def home():
    return render_template("index.html")

# ✅ Ask route
@app.route("/ask", methods=["POST"])
def ask():
    user_input = request.json["message"]

    if "quiz" in user_input.lower():
        mode = "quiz generator"
    elif "explain" in user_input.lower():
        mode = "teacher"
    else:
        mode = "general study helper"

    response = openai.ChatCompletion.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "system",
                "content": f"You are ScholarCore AI working as a {mode}."
            },
            {"role": "user", "content": user_input}
        ]
    )

    return jsonify({
        "reply": response.choices[0].message.content
    })

# ✅ RUN APP
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 10000)))