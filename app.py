from flask import Flask, render_template, request, redirect

app = Flask(__name__)

messages = []

@app.route('/')
def home():
    return render_template('index.html', messages=messages)

@app.route('/send', methods=['POST'])
def send():
    skill = request.form.get('skill', '').strip()
    level = request.form.get('level', '').strip()
    status = request.form.get('status', '').strip()
    if skill and level and status:
        messages.append({"skill": skill, "level": level, "status": status})
    return redirect('/')

@app.route('/delete', methods=['POST'])
def delete_one():
    index_str = request.form.get('index')
    if index_str is not None:
        index = int(index_str)
        if 0 <= index < len(messages):
            messages.pop(index)
    return redirect('/')

@app.route('/delete_selected', methods=['POST'])
def delete_selected():
    indexes = request.form.getlist('delete_indexes')
    indexes = sorted([int(i) for i in indexes], reverse=True)
    for index in indexes:
        if 0 <= index < len(messages):
            messages.pop(index)
    return redirect('/')

@app.route('/delete_all', methods=['POST'])
def delete_all():
    messages.clear()
    return redirect('/')

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
