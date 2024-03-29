from flask import render_template, flash, redirect
from app import app
from app.forms import LoginForm

#routes are different URLs that the application implemnets
#this is so flask knows what to execute when different URLs are requested

#these decorators modify the function that follows them
@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Ian'}
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in portland!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The avengers movie was so cool!'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():   #sees if the fields are valid
        flash('Login requested for user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data))
        return redirect('/index')
    return render_template('login.html', title='Sign In', form=form)
