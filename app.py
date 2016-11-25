# import the Flask class from the flask module
from flask import Flask, render_template, redirect, url_for, request, session, flash, g
#from flask.ext.sqlalchemy import SQLAlchemy
from functools import wraps
import sqlite3
# create the application object
app = Flask(__name__)

app.secret_key = "my precious"
#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///posts.db'
#import config.py
#import os
#app.config.from_object('config.DevelopmentConfig')
app.database = "sample.db"
#create the sqlalchemy object
#db = SQLAlchemy(app)
#from models import *

#login required decorator
def login_required(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return f(*args, **kwargs)
        else:
            flash('You need to login first.')
            return redirect(url_for('login'))
    return wrap

# use decorators to link the function to a url
@app.route('/')
@login_required
def home():
    #posts = db.session.query(BlogPost).all()
    #posts = []
    #try:
    g.db = connect_db()
    cur = g.db.execute('select * from posts')
    posts = [dict(title=row[0], description=row[1] for row in cur.fetchall()]
        #for row in cur.fetchall():
            #posts.append(dict(title=row[1], description=row[2]))
    g.db.close()
    #except sqlite3.OperationalError:
        #flash("You have no database!")
    return render_template('index.html', posts=posts)

@app.route('/welcome')
def welcome():
    return render_template('welcome.html')  # render a template

# route for handling the login page logic
@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != 'admin':
            error = 'Invalid Credentials. Please try again.'
        else:
            session['logged_in'] = True
            flash('You were just logged in!')
            return redirect(url_for('home'))
    return render_template('login.html', error=error)

@app.route('/logout')
@login_required
def logout():
    session.pop('logged_in', None)
    flash('You were just logged out!')
    return redirect(url_for('welcome'))

def connect_db():
    return sqlite3.connect(app.database)

# start the server with the 'run()' method
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
