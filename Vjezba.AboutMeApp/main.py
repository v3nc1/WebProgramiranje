from flask import Flask, render_template
from config import Config
import validators


app = Flask(__name__)
app.debug = True

@app.route("/")
def index():
	ime_i_prezime = Config.name + ' ' + Config.surname
	return render_template("index.html", name = ime_i_prezime)

@app.route("/education")
def obrazovanje():
	ime_i_prezime = Config.name + ' ' + Config.surname
	return render_template("education.html",name = ime_i_prezime)
	
@app.route("/skills")
def vjestine():
	ime_i_prezime = Config.name + ' ' + Config.surname
	return render_template("skills.html",name = ime_i_prezime)

@app.route("/bankAccount")
def bankovni_racun():
	ime_i_prezime = Config.name + ' ' + Config.surname
	ime_banke = Config.banka
	broj_racuna = Config.iban	
	
	if not validators.iban(broj_racuna):
		broj_racuna="Neispravan IBAN!"
		
	return render_template("bankAccount.html",name = ime_i_prezime, banka=ime_banke, iban=broj_racuna)
@app.route("/comments")
def komentari():
	ime_i_prezime = Config.name + ' ' + Config.surname
	return render_template("comments.html",name = ime_i_prezime)

	
if __name__ == "__main__":
	app.run()
