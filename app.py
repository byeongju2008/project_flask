from flask import Flask, render_template, request, redirect

app = Flask(__name__)
messages = []

@app.route('/')
def home():
    skills = ["Python", "HTML", "SQL", "Bash"]
    return render_template('index.html', data=skills, messages=messages)

@app.route('/send', methods=['POST'])
def send():
    skill = request.form.get('skill')
    level = request.form.get('level')
    status = request.form.get('status')
    
    if skill and level and status:
        messages.append(f"{skill} / {level} / {status}")

    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
