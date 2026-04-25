from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.json.get("message")

    if "hello" in user_message.lower():
        bot_reply = "Hey! How can I help you?"
    elif "price" in user_message.lower():
        bot_reply = "Prices depend on location 😄"
    else:
        bot_reply = "I didn't understand that."

    return jsonify({"reply": bot_reply})