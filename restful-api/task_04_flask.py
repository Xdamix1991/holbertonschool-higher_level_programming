#!/usr/bin/python3
"""
this module contains a simple api created with flask
"""

from flask import jsonify, Flask, Request, request

app = Flask(__name__)


users = {}


@app.route('/')
def home():
    return "Welcome to the Flask API!"


@app.route('/data')
def json_respons():
    user = list(users.keys())
    return jsonify(user)


@app.route('/status')
def status():
    return "OK"


@app.route('/users/<username>')
def get_users(username):
    if username not in users:
        return jsonify({"error": "User not found"}), 404
    else:
        return jsonify(users[username])


@app.route('/add_user', methods=['POST'])
def add_user():
    data = request.get_json()
    if not data or 'username' not in data or 'name' not in data:
        return jsonify({"error": "Username is required"}), 400
    username = data['username']
    users[username] = {
        "name": data['name'],
        "age": data.get('age'),
        "city": data.get('city'),
    }
    return jsonify({"message": "User added", "user": users[username]}), 201


if __name__ == "__main__":
    app.run()
