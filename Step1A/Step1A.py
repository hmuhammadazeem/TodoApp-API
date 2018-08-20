from flask import Flask, request, jsonify
from flask_pymongo import PyMongo

app = Flask(__name__)
mongo = PyMongo(app, uri="mongodb://127.0.0.1:27017/Todo-API")


@app.route("/tasks", methods=['GET'])
def get_tasks_list():
    data = mongo.db.tasks.find()
    data_list = [{'title': task["title"], 'description': task["description"], 'done': task["done"]} for task in data]
    return jsonify({'Tasks': data_list})


@app.route('/tasks/<id>', methods=['GET'])
def get_task(_id):
    task = mongo.db.tasks.find_one_or_404({"id": _id})
    return jsonify({'title': task["title"], 'description': task["description"], 'done': task["done"]})


@app.route('/tasks', methods=['POST'])
def add_task():
    mongo.db.tasks.insert(
        {'title': request.form['title'], 'description': request.form['description'], 'done': request.form['done']})
    return 'Success!'


@app.route('/task/<id>', methods=['PUT'])
def update_task(_id):
    tasks = mongo.db.tasks
    task = tasks.find_one({'id': _id})
    task["title"] = request.form['title']
    task["description"] = request.form['description']
    task["done"] = request.form['done']
    tasks.save(task)
    return get_tasks_list()


@app.route('/tasks/<id>', methods=['DELETE'])
def delete_task(_id):
    tasks = mongo.db.tasks
    task = tasks.find_one({'id': _id})
    task.remove()
    return 'Task deleted successfully!'


@app.route('/')
def index():
    return """
    <form action="/todo/api/v1.0/tasks" method="POST">
    <input type="text" name="title" placeholder="title"><br>
    <input type="text" name="description" placeholder="description"><br>
    <input type="text" name="done" placeholder="done"><br>
    <input type="submit" value="Send"> 
    """

if __name__ == '__main__':
    app.run()



