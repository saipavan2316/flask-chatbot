from flask import Flask, render_template, request, jsonify, session
import random

app = Flask(__name__)
app.secret_key = "secret123"

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.json.get("message", "").lower()

    # Start game
    if "start" in user_message:
        number = random.randint(1, 100)
        session['number'] = number
        session['attempts'] = 7

        return jsonify({
            "reply": "🎮 Game started! Guess a number (1–100). You have 7 attempts."
        })

    # If game not started
    if 'number' not in session:
        return jsonify({"reply": "Type 'start' to begin the game."})

    # Convert input
    try:
        guess = int(user_message)
    except:
        return jsonify({"reply": "⚠️ Enter a valid number."})

    number = session['number']
    attempts = session['attempts']

    # Reduce attempts
    attempts -= 1
    session['attempts'] = attempts

    # Hint logic
    diff = abs(number - guess)

    if guess == number:
        session.clear()
        return jsonify({
            "reply": f"🎉 Correct! You won with {attempts} attempts left!"
        })

    if attempts == 0:
        correct = session['number']
        session.clear()
        return jsonify({
            "reply": f"💀 Game over! The number was {correct}. Type 'start' to play again."
        })

    hint = ""
    if diff <= 5:
        hint = "🔥 Very close!"
    elif diff <= 15:
        hint = "😎 Getting closer!"
    else:
        hint = "❄️ Far away!"

    if guess < number:
        direction = "Too low 🔻"
    else:
        direction = "Too high 🔺"

    return jsonify({
        "reply": f"{direction} | {hint} | Attempts left: {attempts}"
    })

if __name__ == "__main__":
    app.run()