from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    #여기에 내 데이터를 만든다!
    my_profile = {
        "name": "송병주",
        "age": "만17,19세"
    }
    # 이제는 JSON이 아니라 HTML 파일을 보냅니다
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)