#!/usr/bin/env python3

from random import randint
from faker import Faker
from app import app
from models import db, Article, User

fake = Faker()

with app.app_context():
    print("Deleting all records...")
    db.session.rollback()  # Rollback any pending transactions
    Article.query.delete()
    User.query.delete()

    print("Creating users...")
    users = []
    usernames = []

    for _ in range(25):
        username = fake.first_name()
        while username in usernames:
            username = fake.first_name()

        usernames.append(username)

        user = User(username=username)
        user.set_password("password123")  # Set a default password for all users
        users.append(user)

    db.session.add_all(users)
    db.session.commit()  # Commit users first to assign IDs

    print("Creating articles...")
    articles = []

    for _ in range(100):
        content = fake.paragraph(nb_sentences=8)
        preview = content[:25] + "..."
        
        article = Article(
            author=fake.name(),  # Consider using user.username if linking to a user
            title=fake.sentence(),
            content=content,
            preview=preview,
            minutes_to_read=randint(1, 20),
        )

        articles.append(article)

    db.session.add_all(articles)
    db.session.commit()
    
    print("Database seeding complete.")
