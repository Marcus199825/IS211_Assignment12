from flask import request, render_template, redirect, flash
import sqlite3
from app import app


@app.route('/student/add', methods=['GET', 'POST'])
def add_student():
    if request.method == 'POST':
        # noinspection PyBroadException
        try:
            first_name = request.form['first_name']
            last_name = request.form['last_name']

            if not first_name or not last_name:
                flash('Both first name and last name are required.', 'error')
                return redirect('/student/add')

            with sqlite3.connect('hw13.db') as connection:
                cursor = connection.cursor()
                cursor.execute('INSERT INTO students (first_name, last_name) VALUES (?, ?)', (first_name, last_name))
                connection.commit()

            flash('Student added successfully.', 'success')
            return redirect('/dashboard')

        except Exception:
            flash('An error occurred while adding the student.', 'error')
            return redirect('/student/add')

    return render_template('NewStudent.html')
