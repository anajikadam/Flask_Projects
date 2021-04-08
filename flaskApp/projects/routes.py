import numpy as np
from flask import render_template, url_for, flash, redirect, request, Blueprint
from flask_login import  current_user, login_required
from flaskApp import db, bcrypt
from flaskApp.models import User, Post
from flaskApp.projects.forms import (RegistrationForm, Form1)


projects = Blueprint('projects', __name__)


@projects.route("/register", methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('main.home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(user)    
        db.session.commit()
        flash('Your account has been created! You are now able to log in', 'success')
        return redirect(url_for('users.login'))
    return render_template('register.html', title='Register', form=form)


@projects.route("/projects_about")
# @login_required
def about():
    return render_template('projects/about.html', title='About')


@projects.route("/Projects")
# @login_required
def projectshome():
    return render_template('projects/home.html', title='Projects | Home')

@projects.route("/Projects_1")
# @login_required
def project_1():
    return render_template('project1/home.html')


@projects.route('/predict1',methods=['POST','GET'])
def predict1():
    from flaskApp.projects.bin.project1.model_1 import PredictSalary
    int_features = [int(x) for x in request.form.values()]
    if int_features:
        final_features = [np.array(int_features)]
        PredictSalaryObj = PredictSalary()
        my_prediction = PredictSalaryObj.predictsal(final_features)
        output = round(my_prediction[0], 2)
        return render_template('project1/project.html',
                           Text ='Employee Salary should be $ {}'
                           .format(output),Data = int_features)
    return render_template('project1/project.html')


@projects.route("/projects1_about")
# @login_required
def about1():
    return render_template('project1/about.html', title='About', show_bar=True)


@projects.route("/Projects_2")
# @login_required
def project_2():
    return render_template('project2/home.html', title='project2 | Home', show_bar = True)


@projects.route('/predict2',methods=['POST','GET'])
def predict2():
    if request.method == 'POST':
        Pregnancies = float(request.form['Pregnancies'])
        Glucose = float(request.form['Glucose'])
        BloodPressure = float(request.form['BloodPressure'])
        SkinThickness = float(request.form['SkinThickness'])
        Insulin = float(request.form['Insulin'])
        BMI = float(request.form['BMI'])
        DiabetesPedigreeFunction = float(request.form['DiabetesPedigreeFunction'])
        Age = float(request.form['Age'])
        data = [[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]]
        # print(data)
        # import pickle
        # filename1 = "flaskApp/projects/bin/project2/models/RFClr.pkl"
        # filename2 = "flaskApp/projects/bin/project2/models/pipeMinSc_StdSc.pkl"
        # model = pickle.load(open(filename1, 'rb'))
        # pipe = pickle.load(open(filename2, 'rb'))
        # trans_data = pipe.transform(data)
        # output = model.predict(trans_data)
        from flaskApp.projects.bin.project2.model_1 import Prediction
        PredObj = Prediction()
        output = PredObj.predict(data)
        prediction = output[0]
        text = "Diabetes"
        if prediction == 0:
            text = "Non Diabetes"
        return render_template('project2/project.html', Data=data, Text=text)
    else:
        return render_template('project2/project.html', title='Project | Home')


@projects.route("/projects2_about")
# @login_required
def about2():
    return render_template('project2/about.html', title='About', show_bar = True)

@projects.route("/Projects_3")
# @login_required
def project_3():
    return render_template('project3/home.html', title='project3 | Home', show_bar = True)


@projects.route('/predict3',methods=['POST','GET'])
def predict3():
    if request.method == 'POST':
        age = float(request.form['age'])
        sex = float(request.form['sex'])
        cp = float(request.form['cp'])
        trestbps = float(request.form['trestbps'])
        chol = float(request.form['chol'])
        fbs = float(request.form['fbs'])
        restecg = float(request.form['restecg'])
        thalach = float(request.form['thalach'])
        exang = float(request.form['exang'])
        oldpeak = float(request.form['oldpeak'])
        slope = float(request.form['slope'])
        ca = float(request.form['ca'])
        thal = float(request.form['thal'])

        data = [[age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]]
        print(data)
        from flaskApp.projects.bin.project3.model_1 import Prediction
        PredObj = Prediction()
        output = PredObj.predict(data)
        prediction = output[0]
        text = "Heart disease"
        if prediction == 0:
            text = "Non Heart disease"
        return render_template('project3/project.html', Data=data, Text=text)
    else:
        return render_template('project3/project.html', title='Project | Home')


@projects.route("/projects3_about")
# @login_required
def about3():
    return render_template('project3/about.html', title='About', show_bar = True)
