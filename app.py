import jsonify

app = Flask(__name__)

coral = [
    {
        'id': 1,
        'title': u'coral1',
        'description': u'The first coral', 
        'done': False
    },
    {
        'id': 2,
        'title': u'coral2',
        'description': u'the secon coral', 
        'done': False
    }
]

@app.route('/todo/api/v1.0/tasks', methods=['GET'])
def get_tasks():
    return jsonify({'coral': coral})

if __name__ == '__main__':
    app.run(debug=True)