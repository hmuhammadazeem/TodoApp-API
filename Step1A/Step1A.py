from flask import Flask, request, jsonify
from flask_pymongo import PyMongo

app = Flask(__name__)
#app.config["MONGO_URI"] = "mongodb://localhost:27017/myDatabase"
#mongo = PyMongo(app)


@app.route("/tasks", methods=['GET'])
def get_tasks_list():
    data_list = list()
    data = mongo.db.tasks.find()
    for x in data:
        data_list.append({'title': x["title"], 'description': x["description"], 'done': x["done"]})
    return jsonify({'Tasks': data_list})


@app.route('/tasks/<id>', methods=['GET'])
def get_task(_id):
    task = mongo.db.tasks.find_one_or_404({"id": _id})
    return jsonify({'title': task["title"], 'description': task["description"], 'done': task["done"]})


@app.route('/tasks', methods=['POST'])
def add_task():



@app.route('/task/<id>', methods=['PUT'])
def update_task(id):
    pass


@app.route('/tasks/<id>', methods=['DELETE'])
def delete_task(id):
    pass

if __name__ == '__main__':
    app.run()





