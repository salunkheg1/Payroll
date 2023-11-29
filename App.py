from flask import Flask,render_template
app = Flask(__name__)
@app.route("/")
def hello_world():
    return render_template('index.html')

@app.route("/Ganesh")
def Ganesh():
    return "<p>Welcome Ganesh___</p>"

@app.route("/about")
def about():
    name = "Ganesh"
    return render_template("about.html",name1=name)

app.run(debug=True)