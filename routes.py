from flask import Flask,render_template,url_for,flash ,redirect
from pythonblog.forms import RegistrationForm,LogInForm
from pythonblog.models import User,Post
from pythonblog import app

posts=[
    {
        'author':'Gaurang jain',
        'title': 'Blog Post 1',
        'content': 'First Post Content',
        'date_poste': 'April 8,2018'

    },
    {
        'author':'Heeral Jain',
        'title': 'Blog Post 2',
        'content': 'Second Post Content',
        'date_poste': 'April 17,2018'
    }

]
@app.route("/")
@app.route("/home")
def home():
    print("SAY MY NAME!!!")
    return render_template('home.html',posts=posts)

@app.route("/register",methods=['Get','Post'])
def register():
    form=RegistrationForm()
    if form.validate_on_submit(): 
        flash(f'Account created for {form.username.data}!','success')
        return redirect(url_for('home'))
    return render_template('register.html',title='Register',form=form)


@app.route("/login")
def login():
    form=LogInForm()
    return render_template('login.html',title='Login',form=form)

@app.route("/about")
def about():
 #   print("SAY MY NAME!!!")
    return render_template('about.html',title='About')
