from flask import Flask, request, redirect, render_template, session, flash

app = Flask(__name__)
app.secret_key = 'your_secret_key'


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username == 'admin' and password == 'password':
            session['logged_in'] = True
            return redirect('/dashboard')
        else:
            flash('Invalid credentials')
    return render_template('Templates/TeacherLogin.html')
