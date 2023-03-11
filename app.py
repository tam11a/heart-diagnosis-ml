from flask import Flask, request, render_template, jsonify
from ml import calculate
import uuid
import json

app = Flask(__name__)


# Load users from JSON file
with open('users.json') as f:
    users = json.load(f)


# Register endpoint
@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    phone = data['phone']
    password = data['password']
    name = data['name']

    # Check if user with phone number already exists
    if any(user['phone'] == phone for user in users['users']):
        return jsonify({'error': 'User with phone number already exists'}), 400

    # Generate unique ID for user
    user_id = str(uuid.uuid4())

    # Add new user
    users['users'].append({
        'id': user_id,
        'phone': phone,
        'password': password,
        'name': name
    })

    # Save updated user data to JSON file
    with open('users.json', 'w') as f:
        json.dump(users, f)

    return jsonify({'message': 'User registered successfully', 'user_id': user_id}), 200


# Login endpoint
@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    phone = data['phone']
    password = data['password']

    # Find user with phone number
    user = next(
        (user for user in users['users'] if user['phone'] == phone), None)

    # Check if user exists and password is correct
    if user and user['password'] == password:
        return jsonify({'message': 'Login successful', 'user_id': user['id']}), 200
    else:
        return jsonify({'error': 'Invalid phone number or password'}), 401


# Profile endpoint
@app.route('/profile', methods=['PUT'])
def profile():
    data = request.get_json()
    user_id = data['user_id']
    password = data['password']
    new_password = data.get('new_password')
    new_name = data.get('name')

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
        "phone": user['phone']
    })


# @app.route('/')
# def show_form():
#     return render_template('form.html')


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
        return jsonify({**result, "name": json.loads(get_profile(user_id).get_data(True))["name"]})
    except:
        return jsonify({'error': 'Something went wrong'}), 400


if __name__ == '__main__':
    app.run(debug=True)
