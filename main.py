from flask import Flask,render_template
app = Flask(__name__)
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


@app.route("/LOGIN.html")
def login():
    return render_template('LOGIN.html')

@app.route("/Ganesh")
def Ganesh():
    return "<p>Welcome Ganesh________</p>"



app.run(debug=True)