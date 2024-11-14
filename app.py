from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/hello', methods=['GET'])
def hello():
    return jsonify({'message': 'Hello, welcome to the API!'})

@app.route('/add', methods=['POST'])
def add():
    data = request.get_json()
    try:
        num1 = data.get('num1', 0)
        num2 = data.get('num2', 0)
        result = num1 + num2
        return jsonify({'result': result})
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@app.route('/user/<int:user_id>', methods=['GET'])
def get_user(user_id):
    users = {
        1: {'name': 'Alice', 'age': 25},
        2: {'name': 'Bob', 'age': 30},
        3: {'name': 'Charlie', 'age': 35}
    }
    
    user = users.get(user_id)
    if user:
        return jsonify(user)
    else:
        return jsonify({'error': 'User not found'}), 404

if __name__ == '__main__':
    app.run()
