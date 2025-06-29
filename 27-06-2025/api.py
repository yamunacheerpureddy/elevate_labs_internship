from flask import Flask, request, jsonify, render_template, redirect, url_for

app = Flask(__name__)

# In-memory storage for users
users = {
    1: {"id": 1, "name": "Naresh", "email": "sunny@example.com"},
    2: {"id": 2, "name": "sandy", "email": "sandy@example.com"},
    3: {"id": 3, "name": "Tarak", "email": "tarak@example.com"},
    4: {"id": 4, "name": "nethra Anadam", "email": "nethra@example.com"},
    5: {"id": 5, "name": "paddu", "email": "paddu@example.com"}
}


# HTML Routes
@app.route('/')
def index():
    return render_template('index.html', users=users.values())


@app.route('/add_user', methods=['GET', 'POST'])
def add_user_page():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        if name and email:
            new_id = max(users.keys()) + 1 if users else 1
            users[new_id] = {"id": new_id, "name": name, "email": email}
            return redirect(url_for('index'))
    return render_template('add_user.html')


@app.route('/edit_user/<int:user_id>', methods=['GET', 'POST'])
def edit_user_page(user_id):
    user = users.get(user_id)
    if not user:
        return redirect(url_for('index'))

    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        if name and email:
            users[user_id] = {"id": user_id, "name": name, "email": email}
            return redirect(url_for('index'))

    return render_template('edit_user.html', user=user)


@app.route('/delete_user/<int:user_id>')
def delete_user_page(user_id):
    if user_id in users:
        del users[user_id]
    return redirect(url_for('index'))


# API Routes
@app.route('/api/users', methods=['GET'])
def get_users():
    return jsonify(list(users.values()))


@app.route('/api/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = users.get(user_id)
    if user:
        return jsonify(user)
    return jsonify({"error": "User not found"}), 404


@app.route('/api/users', methods=['POST'])
def create_user():
    data = request.get_json()
    if not data or 'name' not in data or 'email' not in data:
        return jsonify({"error": "Missing name or email"}), 400

    new_id = max(users.keys()) + 1 if users else 1
    users[new_id] = {"id": new_id, "name": data['name'], "email": data['email']}
    return jsonify(users[new_id]), 201


@app.route('/api/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    user = users.get(user_id)
    if not user:
        return jsonify({"error": "User not found"}), 404

    data = request.get_json()
    if not data or 'name' not in data or 'email' not in data:
        return jsonify({"error": "Missing name or email"}), 400

    users[user_id] = {"id": user_id, "name": data['name'], "email": data['email']}
    return jsonify(users[user_id])


@app.route('/api/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    user = users.get(user_id)
    if not user:
        return jsonify({"error": "User not found"}), 404

    del users[user_id]
    return jsonify({"message": "User deleted successfully"}), 200


if __name__ == '__main__':
    app.run(debug=True)