"""
Part 6: Homework - Personal To-Do List App
==========================================
See Instruction.md for full requirements.

How to Run:
1. Make sure venv is activated
2. Run: python app.py
3. Open browser: http://localhost:5000
"""
""""
from flask import Flask, render_template

app = Flask(__name__)

# Sample data - your tasks list
TASKS = [
    {'id': 1, 'title': 'Learn Flask', 'status': 'Completed', 'priority': 'High'},
    {'id': 2, 'title': 'Build To-Do App', 'status': 'In Progress', 'priority': 'Medium'},
    {'id': 3, 'title': 'Push to GitHub', 'status': 'Pending', 'priority': 'Low'},
]

# Your code here...


if __name__ == '__main__':
    app.run(debug=True)
"""

from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Sample data
TASKS = [
    {'id': 1, 'title': 'Learn Flask', 'status': 'Completed', 'priority': 'High'},
    {'id': 2, 'title': 'Build To-Do App', 'status': 'In Progress', 'priority': 'Medium'},
    {'id': 3, 'title': 'Push to GitHub', 'status': 'Pending', 'priority': 'Low'},
]

# Home page – list all tasks
@app.route('/')
def index():
    return render_template('index.html', tasks=TASKS)

# Add task page
@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        new_task = {
            'id': len(TASKS) + 1,
            'title': request.form['title'],
            'status': request.form['status'],
            'priority': request.form['priority']
        }
        TASKS.append(new_task)
        return redirect(url_for('index'))

    return render_template('add.html')

# Single task detail
@app.route('/task/<int:id>')
def task(id):
    task = next((t for t in TASKS if t['id'] == id), None)
    return render_template('task.html', task=task)

# About page
@app.route('/about/')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True)