from flask import render_template, flash, redirect, url_for
from app import app, db, bcrypt
from app.forms import RegisterForm, SignInForm
from app.models import User, UsersItems, UsersTokens


@app.route('/')
def home():
    games = {
        'cards': ['BlackJack', '3-13'],
        'dice': 'Farcle'
    }
    return render_template('home.jinja', games=games, title='Home')

@app.route('/about')
def about():
    return render_template('about.jinja')

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = SignInForm()
    if form.validate_on_submit():
        if form.email.data: 
            flash(f'You Are Now Loged In', "success")
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check email and password', 'danger')
    return render_template('login.jinja', title='Login', login_form=form)

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data)
        user = User(username=form.username.data, email=form.email.data, password_hash=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash(f'Your account has been created for {form.username.data}!', 'success')
        return redirect(url_for('login'))
    return render_template('register.jinja', title='Register', register_form=form)