import sqlite3

from flask import Flask, session, redirect, render_template

app = Flask(__name__)


@app.route('/dashboard')
def dashboard():
    if not session.get('logged_in'):
        return redirect('/login')
    connection = sqlite3.connect('hw13.db')
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM students')
    students = cursor.fetchall()
    cursor.execute('SELECT * FROM quizzes')
    quizzes = cursor.fetchall()
    connection.close()
    return render_template('Dashboard.html', students=students, quizzes=quizzes)
