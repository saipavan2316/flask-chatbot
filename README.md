# Flask Number Guessing Chatbot

A simple web-based Number Guessing Game built using Flask. The application provides a chatbot-style interface where users can start a game, guess a hidden number between 1 and 100, and receive hints based on how close their guesses are.

## Project URL

https://roadmap.sh/projects/basic-http-server

## Features

* Chatbot-style user interface
* Random number generation between 1 and 100
* 7 attempts per game
* Hot/Cold hint system
* Session-based game state management
* Instant feedback for each guess
* Play again by typing `start`

## How It Works

1. Type `start` to begin a new game.
2. The application generates a random number between 1 and 100.
3. You have 7 attempts to guess the number.
4. After each guess, the chatbot provides:

   * Whether the guess is too high or too low
   * A proximity hint:

     * 🔥 Very close! (difference ≤ 5)
     * 😎 Getting closer! (difference ≤ 15)
     * ❄️ Far away! (difference > 15)
5. If you guess correctly, you win.
6. If all attempts are used, the correct number is revealed.

## Technologies Used

* Python
* Flask
* HTML
* CSS
* JavaScript

## Project Structure

```text
flask-chatbot/
│
├── app.py
├── templates/
│   └── index.html
├── static/
├── requirements.txt
└── README.md
```

## Installation

### Clone the Repository

```bash
git clone https://github.com/your-username/flask-chatbot.git
cd flask-chatbot
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Virtual Environment

Windows:

```bash
venv\Scripts\activate
```

Linux/Mac:

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

## Run the Application

```bash
python app.py
```

Open your browser and visit:

```text
http://127.0.0.1:5000
```

## Example Gameplay

```text
User: start

Bot: Game started! Guess a number (1–100). You have 7 attempts.

User: 50

Bot: Too low 🔻 | Getting closer! | Attempts left: 6

User: 75

Bot: Too high 🔺 | Very close! | Attempts left: 5

User: 72

Bot: Correct! You won with 5 attempts left!
```

## Future Improvements

* Difficulty levels
* Score tracking
* Leaderboard
* Multiple game modes
* User authentication

## Author

Mudrakola Sai Pavan

B.Tech Computer Science and Engineering
Lovely Professional University
