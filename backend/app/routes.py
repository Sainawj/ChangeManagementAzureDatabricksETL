from flask import Blueprint, jsonify, request, session
from flask_login import login_user, logout_user, current_user, login_required
from .models import ChangeRecord, User
from .auth import register_user
from .db import db
from . import login_manager

main = Blueprint('main', __name__)

# User loader function for Flask-Login
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# Home route
@main.route('/')
def index():
    if current_user.is_authenticated:
        return jsonify({"message": f"Welcome, {current_user.email}!"})
    return jsonify({"message": "Welcome to the Change Management Dashboard API"})


# Get all changes (authentication required)
@main.route('/api/changes', methods=['GET'])
@login_required
def get_changes():
    changes = ChangeRecord.query.all()
    return jsonify([{"id": c.id, "change_id": c.change_id, "description": c.description, "status": c.status} for c in changes])


# Add a new change record (authentication required)
@main.route('/api/changes', methods=['POST'])
@login_required
def add_change():
    data = request.json
    new_change = ChangeRecord(change_id=data["change_id"], description=data["description"], status=data["status"])
    db.session.add(new_change)
    db.session.commit()
    return jsonify({"message": "Change record added"}), 201


# Login route
@main.route('/login', methods=['POST'])
def login():
    data = request.json
    user = User.query.filter_by(email=data['email']).first()
    
    if user and user.check_password(data['password']):  # Assuming check_password is a method in your User model
        login_user(user)
        return jsonify({"message": "Login successful!"})
    return jsonify({"message": "Invalid credentials"}), 401


# Logout route
@main.route('/logout')
@login_required
def logout():
    logout_user()
    return jsonify({"message": "Logout successful!"})


# Session check route (for testing purposes)
@main.route('/session')
@login_required
def session_check():
    return jsonify({"message": f"User {current_user.email} is logged in."})

@main.route('/register', methods=['POST'])
def register():
    data = request.json
    email = data['email']
    password = data['password']
    
    # Check if user already exists
    if User.query.filter_by(email=email).first():
        return jsonify({"message": "User already exists"}), 400
    
    # Register the user
    register_user(email, password)
    return jsonify({"message": "User registered successfully"}), 201