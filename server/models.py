from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData
from flask_bcrypt import Bcrypt

metadata = MetaData()
db = SQLAlchemy(metadata=metadata)
bcrypt = Bcrypt()

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, unique=True, nullable=False)
    password_hash = db.Column(db.String, nullable=False)

    def set_password(self, password):
        """Hash and store the user's password"""
        if password:  # Ensure password is not None
            self.password_hash = bcrypt.generate_password_hash(password).decode('utf-8')
        else:
            raise ValueError("Password cannot be empty")

    def check_password(self, password):
        """Check password against stored hash"""
        if not password:  # Prevent NoneType errors
            return False
        return bcrypt.check_password_hash(self.password_hash, password)

class Article(db.Model):
    __tablename__ = 'articles'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    author = db.Column(db.String, nullable=False)
    content = db.Column(db.Text, nullable=False)
    preview = db.Column(db.String, nullable=False)
    minutes_to_read = db.Column(db.Integer, nullable=False)
