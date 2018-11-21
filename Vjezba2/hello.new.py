

from flask import Flask , request , make_response,render_template
from flask_bootstrap import Bootstrap


app = Flask(__name__)
bootstrap=Bootstrap(app)

@app.route('/')
def index():
    return render_template("index.html")



@app.route('/user/<name>')

def user(name):
    
    return render_template("user.html",name=name)

@app.route('/user/')

def nouser():
    
    return render_template("user.html")

@app.route('/req')
def req():
    user_agent = request.headers.get('User-Agent')
    return '<p>Your browser is {0}</p><p>HTTP method is: {1}</p><p></p>'.format(user_agent, request.method)

@app.route('/resp')
def resp():
    r = make_response('<h1>Šaljemo kolačiće!</h1>')
    r.set_cookie('odgovor', '42')
    return r


@app.route('/comments/')

def comments():

    comments=["Jaoo","Koliko","Kada","KO","Zasto"]

    return render_template("comments.html",lista=comments)


@app.errorhandler(404)

def page_not_found(e):
    return render_template("404.html"), 404

@app.errorhandler(500)

def internal_server_error(e):
    return render_template("500.html"), 500