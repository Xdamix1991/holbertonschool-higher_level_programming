#!/usr/bin/python3
"""
this module contains sample api to authetify users and admins
"""
from flask import Flask, jsonify, request
from flask_httpauth import HTTPBasicAuth, HTTPTokenAuth
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import create_access_token, jwt_required, JWTManager
from flask_jwt_extended import get_jwt


app = Flask(__name__)
auth = HTTPBasicAuth()
jwt = JWTManager(app)

app.config['JWT_SECRET_KEY'] = 'key-secret'

users = {
    "user1": {"password": generate_password_hash("password"),
              "role": "user"},
    "admin1": {"password": generate_password_hash("password"),
               "role": "admin"}
}


@auth.verify_password
def verify_password(username, password):
    user = users.get(username)
    if user and check_password_hash(user['password'], password):
        return user
    return None


@app.route('/basic-protected')
@auth.login_required
def access():
    return "Basic Auth: Access Granted"


@app.route('/login', methods=["POST"])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    user = users.get(username)
    if user and check_password_hash(user['password'], password):
        access_token = create_access_token(
            identity=username, additional_claims={"role": user['role']})
        return jsonify(access_token=access_token)
    else:
        return jsonify({"error": "User not found"}), 401


@app.route('/jwt-protected')
@jwt_required()
def protected():
    return "JWT Auth: Access Granted"


@app.route('/admin-only')
@jwt_required()
def admin():
    admin_role = get_jwt()
    if admin_role['role'] == 'admin':
        return "Admin Access: Granted"
    else:
        return jsonify({"error": "Admin access required"}), 403


if __name__ == "__main__":
    app.run()
