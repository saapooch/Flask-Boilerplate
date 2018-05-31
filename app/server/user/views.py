import os
from flask import render_template, Blueprint, request, flash, redirect, url_for, jsonify
from app.server.user.forms import LoginForm, RegisterForm
from flask_login import login_user, logout_user, login_required, current_user
from app.server import db, model, bcrypt
import datetime

basedir = os.path.abspath(os.path.dirname(__file__))
user_blueprint = Blueprint('user', __name__,)

@user_blueprint.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm(request.form)
    if form.validate_on_submit():
        user = model.User.query.filter_by(username=form.username.data).first()
        if user and bcrypt.check_password_hash(
                user.password, request.form['password']):
            login_user(user)
            flash('You are logged in. Welcome!', 'success')
            return redirect(url_for('main.landing'))
        else:
            flash('Invalid email and/or password.', 'danger')
            return render_template('user/login.html', form=form)

    return render_template('user/login.html', form = form)

@user_blueprint.route("/register", methods=['GET', 'POST'])
def register():
    form = RegisterForm(request.form)
    return render_template('user/register.html', form = form)

@user_blueprint.route("/register_confirm", methods=['GET', 'POST'])
def register_confirm():
    form = RegisterForm(request.form)
    if form.validate_on_submit():
        user = model.User(
            username = form.username.data,
            email=form.email.data,
            password=form.password.data
        )
        db.session.add(user)
        db.session.commit()
        login_user(user)
        flash('You are logged in. Welcome!', 'success')
        return redirect(url_for('main.landing'))
    else:
        flash('Incorrect email/password!', 'danger')


@user_blueprint.route("/account/<username>", methods=['GET', 'POST'])
def account(username):
    return render_template('user/account.html')

@user_blueprint.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You were logged out. Bye!', 'success')
    return redirect(url_for('main.landing'))
