from flask import Flask, render_template, request, jsonify # type: ignore
import random

app = Flask(__name__)

# Dictionary to map user input to the corresponding value
youDict = {"s": 1, "w": -1, "g": 0}
# Dictionary to map value to the corresponding name
reverseDict = {1: "Snake", -1: "Water", 0: "Gun"}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/play', methods=['POST'])
def play():
    user_choice = request.json.get('choice')
    if user_choice not in youDict:
        return jsonify({"error": "Invalid choice"}), 400

    user_value = youDict[user_choice]
    computer_value = random.choice(list(youDict.values()))

    result = determine_winner(user_value, computer_value)

    return jsonify({
        "user_choice": reverseDict[user_value],
        "computer_choice": reverseDict[computer_value],
        "result": result
    })

def determine_winner(user, computer):
    if computer == -1 and user == 1:
        return "You Win!"  # Snake drinks water
    elif computer == -1 and user == 0:
        return "You Lose!"  # Gun sinks in water
    elif computer == 1 and user == -1:
        return "You Lose!"  # Snake drinks water
    elif computer == 1 and user == 0:
        return "You Win!"  # Gun kills snake
    elif computer == 0 and user == 1:
        return "You Lose!"  # Gun kills snake
    elif computer == 0 and user == -1:
        return "You Win!"  # Water sinks gun
    else:
        return "It's a Tie!"  # Same choices

if __name__ == '__main__':
    app.run(debug=True)
