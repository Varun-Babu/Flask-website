
from flask import Blueprint, flash, render_template, request, redirect, url_for
from .models import User
from . import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, login_required, logout_user, current_user
from flask_login import LoginManager
# import pandas as pd
# import csv
# import pickle

auth = Blueprint('auth', __name__)

#can imporve prediction with better model
# model = pickle.load(open('svc_test.pkl','rb'))


#login authentication
@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == "POST":
        email = request.form.get('email')
        password = request.form.get('password')

        user = User.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password, password):
                flash('Logged in', category='success')
                login_user(user, remember=True)
                return redirect(url_for('auth.ml'))
            else:
                flash('email doesnt exist', category='error')
    return render_template("login.html")


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('views.home'))


@auth.route('/signup', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        email = request.form.get('email')
        firstName = request.form.get('firstName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')
        user = User.query.filter_by(email=email).first()
        if user:
            flash("Email already exists", category="error")
        elif len(email) < 4:
            flash('Email must be greater than 4 characters.', category='error')
        elif len(firstName) < 2:
            flash('Email must be greater than 2 characters.', category='error')
        elif password1 != password2:
            flash('Password don\'t match.', category='error')
        elif len(password1) < 7:
            flash('Password must be at least 7 characters', category='error')
        else:
            new_user = User(email=email, first_name=firstName, password=generate_password_hash(
                password1, method='sha256'))
            db.session.add(new_user)
            db.session.commit()
            login_user(user, remember=True)

            flash('Account created!', category='success')
            return redirect(url_for('views.home'))
    return render_template("signup.html")


#
#
# @auth.route("/ml")
# def ml():
#csv with predicted taxitime done in jupyternotebook
#     data = pickle.load(open('test_csv.pkl','rb'))
#     myData = list(data.values)
#     return render_template('ml.html',myData = myData)
# def convert(x):
#     return pd.to_datetime(x).strftime('%H:%M:%S')



# #predicting on backend of website with 79.29 % accuracy
# @auth.route("/ml")
# def ml():
#     test_csv = pickle.load(open('test_csv.pkl','rb'))
#     ycsve = test_csv['dept_taxitime']
#     test_csv_eobt = test_csv['eobt']
#     test_csv_aobt = test_csv['aobt']
#     test_csv_atot = test_csv['atot']
#     test_csve = test_csv.drop(['tstamp','acid','dept_taxitime','aircraft_type','bay_number','eobt','aobt','atot'],axis = 1)
#     y_pred = model.predict(test_csve)
#     test_csv['pred_taxitime'] = pd.to_datetime(y_pred, unit='m')
#     test_csv['dept_taxitime'] = pd.to_datetime(test_csv['dept_taxitime'], unit='m').dt.time
#     test_csv['etot'] = pd.to_timedelta(test_csv['aobt'].astype('str')) + test_csv['pred_taxitime']
#     test_csv['pred_taxitime'] = test_csv['pred_taxitime'].dt.time
#     test_csv['etot'] = test_csv['etot'].apply(convert)
#     test_csv['timee'] = test_csv['tstamp'].dt.time
#     test_csv['eobt'] = test_csv_eobt
#     test_csv['aobt'] = test_csv_aobt
#     test_csv['atot'] = test_csv_atot 
#     test_csv = test_csv[['acid','timee','aircraft_type','bay_number','count','eobt','aobt','atot','dept_taxitime','pred_taxitime','etot']]
#     myData = list(test_csv.values)
#     return render_template("ml.html",myData = myData)



