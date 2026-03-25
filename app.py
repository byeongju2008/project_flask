from flask import Flask, render_template
import random

app = Flask(__name__)

activities = [
    "산책하기",
    "영화 보기",
    "운동하기",
    "책 읽기",
    "게임하기"
]

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/recommend")
def recommend():
    activity = random.choice(activities)
    return render_template("result.html", activity=activity)

if __name__ == "__main__":
    app.run(debug=True)