from flask import Flask, request, jsonify
from ml import calculate
import uuid
import json
import os
from flask_cors import CORS

# Path to the folder you want to create
folder_path = "static"

# Check if the folder exists, and create it if it doesn't
if not os.path.exists(folder_path):
    os.makedirs(folder_path)
    print("Static folder created")
else:
    print("Static folder already exists")


app = Flask(__name__)
CORS(app)

# Load users from JSON file
with open('users.json') as f:
    users = json.load(f)


# Register endpoint
@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    email = data['email']
    password = data['password']
    name = data['name']
    gender = data['gender']

    # Check if user with email already exists
    if any(user['email'] == email for user in users['users']):
        return jsonify({'error': 'User with email already exists'}), 400

    # Generate unique ID for user
    user_id = str(uuid.uuid4())

    # Add new user
    users['users'].append({
        'id': user_id,
        'email': email,
        'password': password,
        'name': name,
        'gender': gender
    })

    # Save updated user data to JSON file
    with open('users.json', 'w') as f:
        json.dump(users, f)

    return jsonify({'message': 'User registered successfully', 'user_id': user_id}), 200


# Login endpoint
@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    email = data['email']
    password = data['password']

    # Find user with email
    user = next(
        (user for user in users['users'] if user['email'] == email), None)

    # Check if user exists and password is correct
    if user and user['password'] == password:
        return jsonify({'message': 'Login successful', 'user_id': user['id']}), 200
    else:
        return jsonify({'error': 'Invalid email or password'}), 401


# Profile endpoint
@app.route('/profile', methods=['PUT'])
def profile():
    data = request.get_json()
    user_id = data['user_id']
    password = data['password']
    new_password = data.get('new_password')
    new_name = data.get('name')
    new_gender = data.get('gender')

    # Find user with ID
    user = next(
        (user for user in users['users'] if user['id'] == user_id), None)

    # Check if user exists and password is correct
    if user and user['password'] == password:
        # Update user profile
        if new_password:
            user['password'] = new_password
        if new_name:
            user['name'] = new_name
        if new_gender:
            user['gender'] = new_gender

        # Save updated user data to JSON file
        with open('users.json', 'w') as f:
            json.dump(users, f)

        return jsonify({'message': 'Profile updated successfully'}), 200
    else:
        return jsonify({'error': 'Invalid user ID or password'}), 401


# Endpoint to get user profile information
@app.route('/profile/<user_id>', methods=['GET'])
def get_profile(user_id):

    user = next(
        (user for user in users['users'] if user['id'] == user_id), None)

    if not user:
        return jsonify({'error': 'User not found'}), 404

    return jsonify({
        "id": user['id'],
        "name": user['name'],
        "email": user['email'],
        "gender": user['gender']
    })


@app.route('/calculate', methods=['GET'])
def calculateApi():
    user_id = request.args.get('user_id')
    input_age = request.args.get('age')
    input_systolicBP = request.args.get('systolicBP')
    input_diastolicBP = request.args.get('diastolicBP')
    input_troponin = request.args.get('troponin')
    input_chestpainandpainilefthandnadjaw = request.args.get(
        'chestpainandpainilefthandnadjaw')
    input_ECG = request.args.get('ECG')
    try:
        result = calculate(input_age, input_systolicBP, input_diastolicBP,
                           input_troponin, input_chestpainandpainilefthandnadjaw, input_ECG)
        # return render_template('result.html', score=result['score'], attachment=result['attachment'])
        user = json.loads(get_profile(user_id).get_data(True))
        if not user:
            return jsonify({
                'error': 'User not found'
            }), 404
        return jsonify({**result, "name": user["name"], "gender": user["gender"]})
    except:
        return jsonify({'error': 'Something went wrong'}), 400


if __name__ == '__main__':
    app.run(
        # debug=True
    )
