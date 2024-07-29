# Snake, Water, Gun Game

A simple web-based game where players can choose between Snake, Water, or Gun to play against a computer. The game is built using Flask for the backend and vanilla HTML, CSS, and JavaScript for the frontend.

## Features

- Play against the computer with three choices: Snake, Water, or Gun.
- The computer randomly selects one of the choices.
- Provides feedback on whether you win, lose, or tie based on the rules:
  - Snake drinks Water (Snake beats Water)
  - Gun sinks in Water (Gun loses to Water)
  - Gun kills Snake (Gun beats Snake)

## Prerequisites

- Python 3.x
- Flask

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/Mridul9A/Snake_Water_Gun-Game.git
    cd Snake_Water_Gun-Game
    ```

2. Create and activate a virtual environment:
    ```sh
    python -m venv venv
    source venv/bin/activate   # On Windows use `venv\Scripts\activate`
    ```

3. Install the required packages:
    ```sh
    pip install Flask
    ```

## Running the Application

1. Set the Flask app environment variable:
    ```sh
    export FLASK_APP=app.py    # On Windows use `set FLASK_APP=app.py`
    ```

2. Run the Flask app:
    ```sh
    flask run
    ```

3. Open your web browser and go to `http://127.0.0.1:5000/` to play the game.

## Directory Structure

Snake_Water_Gun-Game/
├── app.py
├── templates/
│ ├── index.html
└── static/
└── style.css


- `app.py`: The main Flask application file that handles game logic and routes.
- `templates/index.html`: The HTML file for the game interface.
- `static/style.css`: The CSS file for styling the game interface.

## Usage

1. Open the game in your web browser.
2. Click one of the buttons to choose Snake, Water, or Gun.
3. The computer will make its choice, and the result will be displayed on the page.
4. The result will indicate whether you won, lost, or tied with the computer.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
