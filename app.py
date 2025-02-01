from flask import Flask, render_template, request, jsonify
import openai
import os

app = Flask(__name__)

# Load API key from environment variable
client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_input = request.form.get("message")  # Use form data instead of JSON
    if not user_input:
        return jsonify({"error": "No input provided"}), 400

    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": user_input}],
        )
        ai_response = response.choices[0].message.content.strip()
        return render_template("index.html", ai_response=ai_response)

    except Exception as e:
        return render_template("index.html", ai_response=f"Error: {str(e)}")


if __name__ == "__main__":
    app.run(debug=True)
