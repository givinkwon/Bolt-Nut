from config import query
from flask import Flask, request, session, redirect, render_template, url_for
import os

app = Flask(__name__)

@app.route('/')
def 

if __name__ == "__main__":
    app.secret_key = os.urandom(12) # for session
    app.run(debug=True, host='0.0.0.0') # https://flask-docs-kr.readthedocs.io/ko/latest/quickstart.html / public ip acess 가능 