from flask import Flask, request, session, redirect, render_template, url_for
import os
import pymysql
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

@app.route('/sign_up', methods=['POST', 'GET'])
def btn_signup():
    error = None
    if request.method == 'POST':
        user_class = request.form['class']
        user_email = request.form['email']
        user_name = request.form['username']
        user_pw = request.form['password']
        user_phone = request.form['phone']
        
        
        conn = pymysql.connect(host='localhost', user='root', password='1234', db='boltnut', charset='utf8')
        cursor = conn.cursor()
        query = "SELECT * FROM user"
        cursor.execute(query)
        data = cursor.fetchall()
        
        
        if data:
            error = "이메일이 이미 존재합니다. 다른 아이디를 사용해주세요."
            return render_template('/accounts/signup.html')
        else:
            cursor.close()
            conn.close()
            return render_template('index.html')
   
            
if __name__ == "__main__":
    app.secret_key = os.urandom(12) # for session
    app.run(debug=True, host='0.0.0.0') # https://flask-docs-kr.readthedocs.io/ko/latest/quickstart.html / public ip acess 가능 