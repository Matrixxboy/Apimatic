from flask import Flask, jsonify

app = Flask(__name__)

# A simple list to act as a mock database
users = [
    {"id": 1, "name": "Alice"},
    {"id": 2, "name": "Bob"},
    {"id": 3, "name": "Charlie"}
]

# Route to get all users
@app.route('/users', methods=['GET'])
def get_users():
    return jsonify(users)

# Route to get a single user by ID
@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    # Find the user with the matching ID
    user = next((item for item in users if item["id"] == user_id), None)
    
    if user:
        return jsonify(user)
    else:
        return jsonify({"error": "User not found"}), 404

# Route to create a new user (example)
@app.route('/users', methods=['POST'])
def create_user():
    # In a real app, you'd get data from request.json
    new_user = {"id": len(users) + 1, "name": "New User"}
    users.append(new_user)
    return jsonify(new_user), 201
@app.route('/bhai', methods=['POST'])
def create_user2():
    # In a real app, you'd get data from request.json
    new_user = {"id": len(users) + 1, "name": "New User"}
    users.append(new_user)
    return jsonify(new_user), 201

# Run the app
if __name__ == '__main__':
    app.run(debug=True)