# getting errors?
# hit (Ctrl+Shift+P).and type Python: Select Interpreter
# the correct interpreter is Python 3.7.X 64 bit (./env/bin/python)
# if that is not an option call jake over

from flask import Flask, render_template, flash, redirect, session, url_for, request, g
from flask_assets import Environment, Bundle

app = Flask(__name__) 

assets = Environment(app)

assets.register({
    'index_js' : Bundle('js/home.js', output='gen/index.js'),
    'index_css' : Bundle('css/main.css', output='gen/index.css'),
    'student_js': Bundle(output = 'gen/student.js'),
    'student_css': Bundle(output = 'gen/student.css'),
    'teacher_js': Bundle(output = 'gen/teacher.js'),
    'teacher_css': Bundle(output = 'gen/teacher.css'),
    'interviewer_js': Bundle(output = 'gen/interviewer.js'),
    'interviewer_css': Bundle(output = 'gen/interviewer.css'),
    'interviewee_js': Bundle(output = 'gen/interviewee.js'),
    'interviewee_css': Bundle(output = 'gen/interviewee.css'),
})

@app.route('/') 
def index(): 
    return render_template('index.html')

@app.route('/student')
def students():
    return render_template('students.html')

@app.route('/teacher')
def teachers():
    return render_template('teacher.html')

@app.route('/interviewer')
def interviewer():
    return render_template('teacher.html')

@app.route('/interviewee')
def interviewee():
    return render_template('interviewee.html')

# main driver function 
if __name__ == '__main__': 
    app.run(debug = True) # change this flag when moving into production