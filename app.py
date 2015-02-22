# adapted with help from https://github.com/lrei
#supposed to be able to work with curl


from flask import Flask, jsonify, abort, request, make_response, url_for

app = Flask(__name__)

corals = [
    {
        'id': 1,
        'name': u'coralone',
        'price': u'25.43', 
        'done': False
    },
    {
        'id': 2,
        'name': u'coral2',
        'price': u'23.32', 
        'done': False
    }
]

@app.route('/coral', methods=['GET'])
def get_tasks():
    return jsonify({'coral': coral})
    

@app.route('/coral', methods=['POST'])
def create_task():
    if not request.json or not 'name' in request.json:
        abort(400)
    task = {
        'id': coral[-1]['id'] + 1,
        'name': request.json['name'],
        'price': request.json.get('price', ""),
        'done': False
    }
    tasks.append(coral)
    return jsonify({'coral': coral}), 201

@app.route('/coral/<int:coral_id>', methods=['PUT'])
def update_task(task_id):
    coral = [coral for coral in corals if coral['id'] == coral_id]
    if len(coral) == 0:
        abort(404)
    if not request.json:
        abort(400)
    if 'nme' in request.json and type(request.json['name']) != unicode:
        abort(400)
    if 'price' in request.json and type(request.json['price']) is not unicode:
        abort(400)
    if 'done' in request.json and type(request.json['done']) is not bool:
        abort(400)
    task[0]['name'] = request.json.get('name', task[0]['name'])
    task[0]['price'] = request.json.get('price', task[0]['price'])
    task[0]['done'] = request.json.get('done', task[0]['done'])
    return jsonify({'coral': coral[0]})

@app.route('/todo/api/v1.0/tasks/<int:coral_id>', methods=['DELETE'])
def delete_coral(coral_id):
    coral = [coral for coral in corals if coral['id'] == coral_id]
    if len(coral) == 0:
        abort(404)
    tasks.remove(coral[0])
    return jsonify({'result': True})


if __name__ == '__main__':
    app.run(debug=True)
