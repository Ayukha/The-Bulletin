from flask import Flask, render_template,request,url_for
from flask_wtf import FlaskForm
from flask_bootstrap import Bootstrap
from wtforms import BooleanField, StringField, PasswordField, validators


app = Flask(__name__)
Bootstrap(app)
app.config['SECRET_KEY']='Itsasecret'
class LoginForm(FlaskForm):
    username = StringField('Username', [validators.Length(min=4, max=25)])
    password = PasswordField('Password',[validators.DataRequired()])
    remember = BooleanField('Remember me')

class RegistrationForm(FlaskForm):
    username = StringField('Username', [validators.Length(min=4, max=25)])
    email = StringField('Email Address', [validators.Length(min=5, max=35)])
    password = PasswordField('New Password',[
        validators.DataRequired(),
        validators.EqualTo('confirm', message='Passwords must match')
    ])
    confirm = PasswordField('Repeat Password')
    remember = BooleanField('Remember me')
    

@app.route('/signup.html', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
   
    return render_template('signup.html', form=form)

@app.route('/')
@app.route('/login.html' ,methods=['GET', 'POST'])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        return render_template('profile.html')
    return render_template('login.html',form=form)

@app.route('/profile.html')
def profile():
	return render_template('profile.html')

if __name__=='__main__':
    	app.run(debug=True)