from flask import Flask, request, jsonify, render_template
from utils import get_answer

app = Flask(__name__)

chat_history = []

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_input = request.json["message"]

    # Add context
    context = " ".join(chat_history[-2:])
    full_query = context + " " + user_input

    response = get_answer(full_query)

    chat_history.append(user_input)
    chat_history.append(response)

    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(debug=True)