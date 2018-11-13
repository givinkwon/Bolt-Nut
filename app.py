from flask import Flask, request, session, redirect, render_template, url_for
import os

app = Flask(__name__)

@app.route('/')
def main():
    return render_template('index.html')

@app.route('/login')
def login():
    return render_template('/accounts/login.html')

@app.route('/signup')
def signup():
    return render_template('/accounts/signup.html')

@app.route('/add_project')
def add_project():
    return render_template('/project/add_project.html')

@app.route('/search_project')
def search_project():
    return render_template('/project/search_project.html')

@app.route('/prepare')
def prepare():
    return render_template('prepare.html')

@app.route('/terms_of_service')
def term_of_service():
    return render_template('terms_of_service.html')

if __name__ == "__main__":
    app.secret_key = os.urandom(12) # for session
    app.run(debug=True, host='0.0.0.0') # https://flask-docs-kr.readthedocs.io/ko/latest/quickstart.html / public ip acess 가능 