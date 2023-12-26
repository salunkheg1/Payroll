from flask import Flask,render_template,request
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/payroll'
db = SQLAlchemy(app)

class User(db.Model):
    USER_ID = db.Column(db.Integer, primary_key=True)
    USER_NAME = db.Column(db.String(80), nullable=False)
    PASSWORD = db.Column(db.String(12), nullable=False)
    ROLL = db.Column(db.String(120), nullable=False)


@app.route("/")
def home():
    return render_template('index.html')

@app.route("/index.html")
def index():
    return render_template('index.html')

@app.route("/about.html")
def about():
    return render_template('about.html')

@app.route("/contact.html")
def contact():
    return render_template('contact.html')

@app.route("/post.html")
def post():
    return render_template('post.html')



@app.route("/login.html", methods = ['GET', 'POST'])
def login():
    roll="ADMIN"
    if(request.method=='POST'):
        name = request.form.get('username')
        password = request.form.get('password')
        entry = User(USER_NAME = name, PASSWORD = password , ROLL=roll)
        db.session.add(entry)
        db.session.commit()
    return render_template('login.html')



@app.route("/Ganesh")
def Ganesh():
    return "<p>Welcome Ganesh________</p>"



app.run(debug=True)