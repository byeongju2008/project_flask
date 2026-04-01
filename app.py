from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    #여기에 내 데이터를 만든다!
    my_profile = {
        "name": "송병주",
        "age": "18",
        "school": "종로산업정보학교",
        "hobby": "게임, 그림, 음악"

    }

    # 이제는 JSON이 아니라 HTML 파일을 보냅니다
    return render_template('index.html', data=my_profile)

if __name__ == '__main__':
    app.run(debug=True)