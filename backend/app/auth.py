from werkzeug.security import generate_password_hash
from .models import User
from .db import db

# Register a new user
def register_user(email, password):
    password_hash = generate_password_hash(password)
    new_user = User(email=email, password_hash=password_hash)
    db.session.add(new_user)
    db.session.commit()
