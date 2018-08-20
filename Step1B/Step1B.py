from flask import Flask, request, jsonify


app = Flask(__name__)


@app.route("/tasks", methods=['GET'])
def get_tasks_list():
	pass


@app.route('/tasks/<id>', methods=['GET'])
def get_task(_id):
	pass

@app.route('/tasks', methods=['POST'])
def add_task():
	pass


@app.route('/task/<id>', methods=['PUT'])
def update_task(id):
    pass


@app.route('/tasks/<id>', methods=['DELETE'])
def delete_task(id):
    pass

if __name__ == '__main__':
    app.run()





