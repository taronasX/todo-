from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# 仮のデータベースとしてのリスト
todos = []

@app.route('/')
def index():
    return render_template("index.html", todos=todos)

@app.route('/add', methods=['POST'])
def add_todo():
    title = request.form.get("title")
    todos.append({"title": title, "complete": False})
    return redirect(url_for("index"))

@app.route('/update/<int:todo_id>')
def update_todo(todo_id):
    todos[todo_id]["complete"] = not todos[todo_id]["complete"]
    return redirect(url_for("index"))

@app.route('/delete/<int:todo_id>')
def delete_todo(todo_id):
    del todos[todo_id]
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(debug=True)

