from flask import Flask, request, jsonify
from flask_pymongo import PyMongo
import json

app = Flask(__name__)
mongo = PyMongo(app, uri="mongodb://127.0.0.1:27017/Todo-API")


@app.route("/tasks", methods=['GET'])
def get_tasks_list():
    data = mongo.db.tasks.find()
    data_list = [{'_id': int(task["_id"]), 'title': task["title"],
                  'description': task["description"], 'done': task["done"]} for task in data]
    return jsonify({'Tasks': data_list})


@app.route('/tasks/<int:ID>', methods=['GET'])
def get_task(ID):
    task = mongo.db.tasks.find_one_or_404({'_id': ID})
    return jsonify({'_id': int(task['_id']),
                    'title': task["title"], 'description': task["description"], 'done': task["done"]})


@app.route('/tasks/add', methods=['POST'])
def add_task():
    mongo.db.tasks.insert(
        {'_id': get_task_id(), 'title': request.form['title'],
         'description': request.form['description'], 'done': request.form['done']})
    return 'Success!'


@app.route('/tasks/update/<int:ID>', methods=['PUT'])
def update_task(ID):
    tasks = mongo.db.tasks
    task = tasks.find_one({'_id': ID})
    data = request.get_json()
    for x in data.keys():
        task[x] = data[x]
    tasks.save(task)
    return get_tasks_list()


@app.route('/tasks/delete/<int:ID>', methods=['DELETE'])
def delete_task(ID):
    mongo.db.tasks.delete_one({'_id': ID})
    return 'Task deleted successfully!'


@app.route('/')
def index():
    return """
    <form action="/tasks/add" method="POST">
        <input type="text" name="title" placeholder="Title"><br>
        <input type="text" name="description" placeholder="Description"><br>
        <input type="text" name="done" placeholder="Status"><br>
        <input type="submit" value="Add"> 
    </form>
    """


# function written to provide the functionality of auto-number feature of SQL
def get_task_id():
    value = mongo.db.counter
    id = value.find_one({'_id': 'taskid'})
    x = id['sequence_value']
    id['sequence_value'] += 1
    value.save(id)
    return x


if __name__ == '__main__':
    app.run()





