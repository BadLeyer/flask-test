# -*- coding: utf-8 -*-
from flask import Flask
from flask import render_template,session,redirect,url_for,request

app = Flask(__name__)

"""ウェルカム画面"""
@app.route('/')
@app.route('/Welcom')
def welcom():
    return render_template('welcom.html')

"""サインアップ画面"""
@app.route('/Signup')
def signUp():
    return render_template('signup.html')

"""サインアップ登録画面"""
@app.route('/SignupComfirm',methods=['GET','POST'])
def signUpComfirm():
    if request.method = 'GET':
        pass
    elif request.method = 'POST':
        
    return redirect(url_for('Welcom'))
    

"""サインイン画面"""
@app.route('/Signin')
def signIn():
    return render_template('sign_up.html')

"""サインイン確認画面"""
@app.route('/SigninComfirm',methods=['GET','POST'])
def signinComfirm():
    return render_template(url_for('Home'))

"""ホーム画面"""
@app.route('/Home')
def home():
    return render_template('home.html')

if __name__ == '__main__':
    app.run()

