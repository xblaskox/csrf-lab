#!/usr/bin/env python3
from flask import Flask, request, make_response, redirect

app = Flask(__name__)
users = {'blasko': 'hunter2'}

@app.route('/')
def home():
    return '<h2>Welcome, blasko!</h2><a href="/change-password">Change Password</a>'

@app.route('/login')
def login():
    resp = make_response(redirect('/'))
    resp.set_cookie('auth', 'blasko')
    return resp

@app.route('/change-password', methods=['GET', 'POST'])
def change_password():
    auth = request.cookies.get('auth')
    if auth != 'blasko':
        return "Unauthorized", 401

    if request.method == 'POST':
        new_password = request.form.get('new_password')
        users['blasko'] = new_password
        return f"Password changed to: {new_password}"
    
    return '''
        <form method="POST">
            <input name="new_password" placeholder="New password">
            <input type="submit" value="Change">
        </form>
    '''

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)

