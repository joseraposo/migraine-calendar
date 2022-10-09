from flask import render_template, flash, redirect, url_for
from flask_login import login_user, current_user, logout_user, login_required
from migraine_calendar import app, bcrypt
from migraine_calendar.forms import RegistrationForm, LoginForm, MigraineForm, SleepForm
import migraine_calendar.repository as repo

app.config['SECRET_KEY'] = '53ebc891254c13455ca4855d26d5ee90'


@app.route("/", methods=['GET'])
@app.route("/home", methods=['GET'])
@login_required
def home():
    # migraines = repo.get_all_migraines()
    return render_template('home.html')


@app.route("/register", methods=['GET', 'POST'])
@login_required
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        repo.add_new_user_form(form.username.data, hashed_password)
        flash(f'{form.username.data} has been created, and can now login!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title="Register", form=form)


@app.route("/login", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = repo.get_user_by_name(form.username.data)
        if user and bcrypt.check_password_hash(user.password_hash, form.password.data):
            login_user(user, remember=form.remember.data)
            return redirect(url_for('home'))
    return render_template('login.html', title="Login", form=form)


@app.route("/logout", methods=['GET'])
def logout():
    logout_user()
    return redirect(url_for('login'))


@app.route("/add_migraine", methods=['GET', 'POST'])
@login_required
def add_migraine():
    form = MigraineForm()
    if form.validate_on_submit():
        flash(f'Migraine created successfully!', 'success')
        # return  # created migraine
        return render_template('add_migraine.html', title="Add Migraine", form=form)
    return render_template('add_migraine.html', title="Add Migraine", form=form)


@app.route("/add_sleep", methods=['GET', 'POST'])
@login_required
def add_sleep():
    form = SleepForm()
    if form.validate_on_submit():
        flash(f'Sleep created successfully!', 'success')
        # return  # created migraine
        return render_template('add_sleep.html', title="Add Sleep", form=form)
    return render_template('add_sleep.html', title="Add Sleep", form=form)