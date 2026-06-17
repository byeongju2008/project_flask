from flask import Flask, render_template, request, redirect

app = Flask(__name__)

messages = []
next_id = 1

@app.route('/')
def home():
    return render_template('index.html', messages=messages)

@app.route('/send', methods=['POST'])
def send():
    global next_id

    skill = request.form.get('skill', '').strip()
    level = request.form.get('level', '').strip()
    status = request.form.get('status', '').strip()

    if not skill or not level or not status:
        return redirect('/')

    messages.append({
        "id": next_id,
        "skill": skill,
        "level": level,
        "status": status
    })

    next_id += 1
    return redirect('/')

@app.route('/delete/<int:item_id>', methods=['POST'])
def delete(item_id):
    global next_id
    for item in messages:
        if item["id"] == item_id:
            messages.remove(item)
            break
            
    # 개별 삭제 후 데이터가 하나도 남지 않았다면 id를 1로 초기화
    if not messages:
        next_id = 1

    return redirect('/')

@app.route('/delete_all', methods=['POST'])
def delete_all():
    global next_id
    messages.clear()
    next_id = 1  # 전체 삭제 시 다음 ID를 1로 초기화합니다.
    return redirect('/')

@app.route('/delete_selected', methods=['POST'])
def delete_selected():
    global next_id
    selected_ids = request.form.getlist('selected_ids')
    remaining_messages = []

    for item in messages:
        if str(item["id"]) not in selected_ids:
            remaining_messages.append(item)

    messages.clear()
    for item in remaining_messages:
        messages.append(item)
        
    # 선택 삭제 후 데이터가 하나도 남지 않았다면 id를 1로 초기화
    if not messages:
        next_id = 1

    return redirect('/')

@app.route('/edit/<int:item_id>')
def edit(item_id):
    target_item = None
    for item in messages:
        if item["id"] == item_id:
            target_item = item
            break

    if target_item is None:
        return redirect('/')

    return render_template('edit.html', item=target_item)

@app.route('/update/<int:item_id>', methods=['POST'])
def update(item_id):
    target_item = None
    for item in messages:
        if item["id"] == item_id:
            target_item = item
            break

    if target_item is None:
        return redirect('/')

    skill = request.form.get('skill', '').strip()
    level = request.form.get('level', '').strip()
    status = request.form.get('status', '').strip()

    if not skill or not level or not status:
        return redirect(f'/edit/{item_id}')

    target_item["skill"] = skill
    target_item["level"] = level
    target_item["status"] = status

    return redirect('/')

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
