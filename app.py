from flask import Flask, render_template,request,url_for,session,logging,g,redirect
from flask_wtf import FlaskForm
from flask_bootstrap import Bootstrap
from wtforms import BooleanField, StringField, PasswordField, validators
from flask_admin import Admin
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
 
Bootstrap(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///students.db'
app.config['SECRET_KEY']='Itsasecret'

db = SQLAlchemy(app)

class TestModel(db.Model):
    id = db.Column('test_id',  db.Integer, primary_key = True)
    name = db.Column(db.String(100))

    def __init__(self, name):
        self.name = name

class students(db.Model):
   id = db.Column('student_id', db.Integer, primary_key = True)
   username = db.Column(db.String(100))
   email = db.Column(db.String(50),unique=True)
   password = db.Column(db.String(200)) 
   


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
    




admin = Admin(app, name='BULLETIN', template_mode='bootstrap3')







@app.route('/signup', methods=['GET', 'POST'])
def signup():
    form = RegistrationForm()

    if form.validate_on_submit():
        new_user = students(username=form.username.data,email=form.email.data,password=form.password.data)
        db.session.add(new_user)
        db.session.commit()
        return render_template('login.html')
    return render_template('signup.html', form=form)







@app.route('/',methods=['GET', 'POST'])
@app.route('/login' ,methods=['GET', 'POST'])
def login():
    if request.method == 'POST' :
        session.pop('user', None)
    form = LoginForm()
    if form.validate_on_submit():
        user=students.query.filter_by(username=form.username.data).first()
        if user:
            if user.password == form.password.data:
                session['user'] = form.username
                return redirect(url_for('profile')) 
    return render_template('login.html',form=form)





@app.before_request
def before_request():
    g.user=None
    if 'user' in session:
        g.user = session['user']




@app.route('/profile')
def profile():
    if g.user:
	   return render_template('profile.html')
    return render_template('login.html',form=form)




@app.route('/student_notice')
def student_discussion():
    return render_template('student_notices.html')




@app.route('/student_discussion')
def pstudent_inventory():
    return render_template('student_discussion.html')



@app.route('/student_inventory')
def student_notice():
    return render_template('student_inventory.html')



@app.route('/profile.html')
def cr_discussion():
    return render_template('profile.html')




@app.route('/profile.html')
def cr_inventory():
    return render_template('profile.html')





@app.route('/profile.html')
def cr_notices():
    return render_template('profile.html')





@app.errorhandler(404)
def page_not_found(e):
    return render_template('error.html'), 404






if __name__=='__main__':

    db.create_all()
    app.run(debug=True)