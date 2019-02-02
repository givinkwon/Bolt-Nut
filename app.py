# -*- coding: utf-8 -*-

from flask import Flask, request, session, redirect, render_template, url_for
from werkzeug import secure_filename
import os
import pymysql
import json
app = Flask(__name__)

@app.route('/')
def main():
    session = {}
    return render_template('index.html')

@app.route('/login')
def login():
    return render_template('/accounts/login.html')

@app.route('/signup')
def signup():
    return render_template('/accounts/signup.html')

@app.route('/add_project')
def add_project():
     if not session == {}:
        return render_template('/project/add_project.html')
     else:
        return render_template('/accounts/login.html')

# 새로운 프로젝트 제출 처리
@app.route('/submit_project', methods = ['GET', 'POST'])
def submit_project():
    if request.method == 'POST':
        project_category = request.form['project_category']
        project_title = request.form['project_title']
        project_period = request.form['project_period']
        project_budget = request.form['project_budget']
        project_state = request.form['project_state']
        project_content = request.form['project_content']
        project_finish = request.form['project_finish']
        project_meeting = request.form['project_meeting']
        project_location = request.form['project_location']
        project_location_detail = request.form['project_location_detail']
        project_start = request.form['project_start']
        project_experience = request.form['project_experience']
        project_goverment = request.form['project_goverment']
        f = request.form.get('file',False)
        if project_title is '':
            error = "프로젝트 제목을 입력해주세요"
            return render_template('/project/add_project.html', error=error, project_period=project_period, project_budget=project_budget, project_content=project_content, project_finish=project_finish, project_location_detail=project_location_detail, project_start=project_start)
        
        if project_period is '':
            error = "예상 기간을 입력해주세요"
            return render_template('/project/add_project.html', error=error, project_title=project_title, project_budget=project_budget, project_content=project_content, project_finish=project_finish, project_location_detail=project_location_detail, project_start=project_start)
        
        if project_budget is '':
            error = "지출 가능 예산을 입력해주세요"
            return render_template('/project/add_project.html', error=error, project_period=project_period, project_title=project_title, project_content=project_content, project_finish=project_finish, project_location_detail=project_location_detail, project_start=project_start)
        
        if project_content is '':
            error = "프로젝트 내용을 입력해주세요"
            return render_template('/project/add_project.html', error=error, project_period=project_period, project_title=project_title, project_budget=project_budget, project_finish=project_finish, project_location_detail=project_location_detail ,project_start=project_start)
       
        if project_finish is '':
            error = "모집 마감 일자를 입력해주세요"
            return render_template('/project/add_project.html', error=error, project_period=project_period, project_title=project_title, project_budget=project_budget, project_content=project_content, project_location_detail=project_location_detail ,project_start=project_start)
         
        if project_location_detail is '':
            error = "클라이언트 위치를 입력해주세요"
            return render_template('/project/add_project.html', error=error, project_period=project_period, project_title=project_title, project_budget=project_budget, project_content=project_content, project_finish=project_finish ,project_start=project_start)
        
        if project_start is '':
            error = "예상시작일을 입력해주세요"
            return render_template('/project/add_project.html', error=error, project_period=project_period, project_title=project_title, project_budget=project_budget, project_content=project_content, project_finish=project_finish ,project_location_detail=project_location_detail)
        
        if f is '':
            error = "검수를 위한 기획/사진/데이터를 첨부해주세요"
            return render_template('/project/add_project.html', error=error, project_period=project_period, project_title=project_title, project_budget=project_budget, project_content=project_content, project_finish=project_finish ,project_location_detail=project_location_detail, project_start=project_start)
        else:
            file = request.files['file']
           
            l=session['username']+file.filename
         
            file.save('C:/Users/rlqls/Documents/GitHub/Bolt-Nut/file/'+l)
            conn = pymysql.connect(host='localhost', user='root', password='123456789', db='boltnut', charset='utf8')
            cursor = conn.cursor()
            query = "INSERT INTO project (project_category, project_title, project_period, project_budget, project_state,  project_content, project_finish, project_meeting, project_location, project_location_detail, project_start, project_experience, project_goverment,file, permit) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, 0)"
            value = (project_category, project_title, project_period, project_budget, project_state,  project_content, project_finish, project_meeting, project_location, project_location_detail, project_start, project_experience, project_goverment, l)
            cursor.execute(query, value)
            conn.commit()
            return render_template('/project/project_enroll.html')

@app.route('/expert')
def expert ():
    return render_template('prepare.html')

@app.route('/profile')
def profile ():
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
        
        if user_email is '':
            error = "이메일을 입력해주세요"
            return render_template('/accounts/signup.html', error=error)
            
        if user_name is '':
            error = "아이디를 입력해주세요"
            return render_template('/accounts/signup.html', error=error)
        
        if user_pw is '':
            error = "비밀번호를 입력해주세요"
            return render_template('/accounts/signup.html', error=error)
        
        if user_phone is '':
            error = "전화번호를 입력해주세요"
            return render_template('/accounts/signup.html', error=error)
        
        conn = pymysql.connect(host='localhost', user='root', password='123456789', db='boltnut', charset='utf8')
        cursor = conn.cursor()
        query = "SELECT * FROM user WHERE user_name = '%s'"% (user_name)
        cursor.execute(query)
        
        data = cursor.fetchall()
        
        if data:
            error = "아이디가 이미 존재합니다. 다른 아이디를 사용해주세요."
            return render_template('/accounts/signup.html', error=error)
        else:
            query = "INSERT INTO user(user_class, user_email, user_name, user_password, user_phone) VALUES (%s, %s, %s, %s, %s)"
            value = (user_class, user_email, user_name, user_pw, user_phone)
            cursor.execute(query, value)
            conn.commit()
            return render_template('/accounts/login.html')

        
@app.route('/login_action', methods=['POST', 'GET'])
def btn_login():
    error = None
    if request.method == 'POST':
        user_name = request.form["username"]
        user_pw = request.form['password']
        conn = pymysql.connect(host='localhost', user='root', password='123456789', db='boltnut', charset='utf8')
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        query = "SELECT * FROM user WHERE user_name = '%s' AND user_password = '%s'"% (user_name, user_pw)
        cursor.execute(query)
        data = cursor.fetchall()
        
        if data:
            for row in data:
                session['class'] = row['user_class']
            session['username'] = request.form["username"]
            return render_template('index.html')
        else:
            error = "아이디나 비밀번호가 잘못되었습니다."
            return render_template('/accounts/login.html', error=error)
        
@app.route('/search_project')
def search_project():
    return render_template('/project/search_project.html')

@app.route('/search_project2', methods=["POST"])
def search_project2():
    conn = pymysql.connect(host='localhost', user='root', password='123456789', db='boltnut', charset='utf8')
    cursor = conn.cursor()
    query = "SELECT * FROM project WHERE permit = '1' ORDER BY project_id DESC"
    cursor.execute(query)
    data = json.dumps(cursor.fetchall())
    return data

@app.route('/project_detail', methods=["POST","GET"])
def project_detail():
    project_id = request.args.get('id')
    return render_template('/project/project_detail.html', project_id=project_id)

@app.route('/project_detail2', methods=["POST","GET"])
def project_detail2():
    project_id = request.form['project_id']
    conn = pymysql.connect(host='localhost', user='root', password='123456789', db='boltnut', charset='utf8')
    cursor = conn.cursor()
    query = "SELECT * FROM project WHERE project_id = '%s' ORDER BY project_id DESC"% (project_id)
    cursor.execute(query)
    data = json.dumps(cursor.fetchall())
    return data
        
@app.route('/logout')
def btn_logout():
    session.clear()
    return render_template('index.html')
            
if __name__ == "__main__":
    app.secret_key = os.urandom(12) # for session
    app.run(debug=True, host='0.0.0.0') # https://flask-docs-kr.readthedocs.io/ko/latest/quickstart.html / public ip acess 가능 