from flask import render_template, flash, redirect, url_for
from migraine_calendar import app
from migraine_calendar.forms import RegistrationForm, LoginForm
import migraine_calendar.repository as repo

app.config['SECRET_KEY'] = '53ebc891254c13455ca4855d26d5ee90'


@app.route("/", methods=['GET'])
@app.route("/home", methods=['GET'])
def home():
    migraines = repo.get_all_migraines()
    return render_template('home.html', migraines=migraines)


@app.route("/about", methods=['GET'])
def about():
    return render_template('about.html', title="About")


@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title="Register", form=form)


@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@migration.com' and form.password.data == 'password':
            flash('You have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')
    return render_template('login.html', title="Login", form=form)
