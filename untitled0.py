# -*- coding: utf-8 -*-
"""
Created on Sun Mar  3 07:12:33 2024

@author: Admin
"""

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///example.db'  # SQLite database, replace with your database URI
db = SQLAlchemy(app)

# Define a basic model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username

@app.route('/')
def index():
    # Create a new user and add it to the database
    new_user = User(username='john')
    db.session.add(new_user)
    db.session.commit()

    # Query all users and print them
    users = User.query.all()
    return '<br>'.join([user.username for user in users])

if __name__ == '__main__':
    app.run(use_reloader=False)
