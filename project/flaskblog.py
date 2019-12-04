from flask import Flask, render_template, url_for, flash, redirect
from flask_sqlalchemy import SQLAlchemy
from forms import RegistrationForm, LoginForm
app = Flask(__name__)

app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

db = SQLAlchemy(app)

class User(db.Model):
    website = db.Column(db.String(30), primary_key=True)
    id = db.Column(db.Integer, unique=True, nullable=False)
    username = db.Column(db.String(20),  unique=True, nullable=False)
    password =  db.Column(db.String(32),  unique=True, nullable=False)

    def __repr__(self):
        return 
    def __str__(self):
        return f"User('{self.username}', '{self.password}')"

posts = [
    {
        'username': 'Swapnil Raj',
        'email_id': 'user1@gmail.com',
        'content': 'Swapnil\'s Secure Vault',
        'date_joined': 'Nov 26, 2019'
        
    },
    {
        'username': 'Vikramaditya Singh',
        'email_id': 'user2@gmail.com',
        'content': 'Vikram\'s secure Vault',
        'date_joined': 'Nov 26, 2019'
    },
    {
        'username': 'Halani Parth',
        'email_id': 'user3@gmail.com',
        'content': 'Parth\'s Secure Vault',
        'date_joined': 'Nov 26, 2019'
    }
]


@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)


@app.route("/about")
def about():
    return render_template('about.html', title='About')


@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)


@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash('You have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')
    return render_template('login.html', title='Login', form=form)


if __name__ == '__main__':
    app.run(debug=True)