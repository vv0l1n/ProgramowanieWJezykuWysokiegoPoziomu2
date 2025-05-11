from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

tasks = [
    {"id": 1, "task": "Zrobić zakupy", "done": False},
    {"id": 2, "task": "Nauka Pythona", "done": False}
]

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/tasks')
def task_list():
    return render_template('tasks.html', tasks=tasks)

@app.route('/add', methods=['POST'])
def add_task():
    task_name = request.form.get('task')
    if task_name:
        new_task = {"id": len(tasks) + 1, "task": task_name, "done": False}
        tasks.append(new_task)
    return redirect(url_for('task_list'))

@app.route('/done/<int:task_id>')
def mark_done(task_id):
    task = next((task for task in tasks if task["id"] == task_id), None)
    if task:
        task["done"] = True
    return redirect(url_for('task_list'))

@app.route('/delete/<int:task_id>')
def delete_task(task_id):
    global tasks
    tasks = [task for task in tasks if task["id"] != task_id]
    return redirect(url_for('task_list'))

if __name__ == '__main__':
    app.run(debug=True)
