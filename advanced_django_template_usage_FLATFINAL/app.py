from flask import Flask, render_template

app = Flask(__name__)

# List of exercises / scripts in your python_work repo
PROJECTS = [
    {
        "name": "Exercise 1: Data Types and Variables",
        "description": "Introductory Python exercise focusing on basic data types, variables, and simple operations.",
        "code_url": "https://github.com/Yochanna/python_work/blob/main/exercise_1.py"
    },
    {
        "name": "Exercise 2: Conditionals and Loops",
        "description": "Practice with if/else statements and for/while loops.",
        "code_url": "https://github.com/Yochanna/python_work/blob/main/exercise_2.py"
    },
    # Add more entries here as needed
]

@app.route("/")
def index():
    return render_template("index.html", projects=PROJECTS)

if __name__ == "__main__":
    app.run(debug=True)