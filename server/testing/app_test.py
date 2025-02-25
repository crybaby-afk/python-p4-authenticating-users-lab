import pytest
from app import app, db, User

@pytest.fixture
def client():
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
    app.config['WTF_CSRF_ENABLED'] = False  # Disable CSRF for testing

    with app.app_context():
        db.create_all()  # Create the test database
        yield app.test_client()
        db.session.remove()
        db.drop_all()  # Cleanup the test database

def test_logs_user_in(client):
    """logs user in by username and adds user_id to session at /login."""
    user = User(username="testuser", password="password123")
    db.session.add(user)
    db.session.commit()

    response = client.post("/login", json={"username": "testuser", "password": "password123"})
    assert response.status_code == 200
    assert b"user_id" in response.data  # Ensure session stores user_id

def test_logs_user_out(client):
    """removes user_id from session at /logout."""
    response = client.post("/logout")
    assert response.status_code == 200
    assert b"Logged out" in response.data

def test_checks_session(client):
    """checks session for user_id at /check_session."""
    user = User(username="testuser", password="password123")
    db.session.add(user)
    db.session.commit()

    client.post("/login", json={"username": "testuser", "password": "password123"})
    response = client.get("/check_session")
    assert response.status_code == 200
    assert b"testuser" in response.data  # Ensure the correct user is returned
