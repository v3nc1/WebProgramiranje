from flask import Flask, render_template, request
from werkzeug.datastructures import MultiDict
from wtforms import Form, Label, PasswordField, StringField, SubmitField

app = Flask(__name__)
app.debug = True

class LoginForm(Form):
    username = StringField('Username:')
    passwd = PasswordField('Password:')
    sbmt = SubmitField('Pošalji')


@app.route("/",methods=['get','post'])
def index():

    msg=""
	
    if request.method=='POST':
        username=request.form["username"]
        passwd=request.form["passwd"]
        if username=="franjo@unizd.hr" and passwd == "123":
            msg="Podaci OK"
        else:
            msg="Pogrešni podaci" 

    return render_template("form.html", message=msg)

@app.route("/form_a",methods=['get','post'])
def index_a():

    msg = ''
    form = LoginForm(MultiDict([('username', ''),('password', '')]))
    if request.method == 'POST':
        username = request.form["username"]
        passwd = request.form["passwd"]
        form = LoginForm(MultiDict([('username', username),('password', passwd)]))
        if username == 'you' and passwd == 'flask':
            msg = 'Username and password are correct'
        else:
            msg = 'Username or password are incorrect'
    return render_template('form_a.html', form=form, message=msg)


if __name__ == "__main__":
	app.run()
