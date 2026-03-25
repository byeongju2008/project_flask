from flask import Flask, render_template
import random

app = Flask(__name__)

@app.route("/")
def my_profile():
    return{
        "name":"송병주",
        "role":"초보 서버 개발자",
        "status":"로컬 환경 통제 완료!",
        "skills":["Ubuntu","VS Code","Python","Flask"],
    }

if __name__ == "__main__":
    app.run(debug=True)