from app.auth import bp as app
from app.models import User
from app.auth.forms import LoginForm
from flask import (redirect, url_for, render_template, flash)
from flask_login import (login_user, logout_user, current_user)

@app.route('/register', methods=['GET', 'POST'])
def register():
    return render_template('auth/register.html', title="Register")

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('main.index'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('main.index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('auth.login'))

        login_user(user, remember=form.remember_me.data)
        return redirect(url_for('main.index'))
    return render_template('auth/login.html', title='Login', form=form)