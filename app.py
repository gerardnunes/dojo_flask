
from distutils.log import debug
from markupsafe import escape
from flask import Flask
from flask import url_for
from flask import redirect, url_for


app= Flask(__name__)


@app.route("/")
def menu():
    return 'menu principal'

@app.route("/nick/<nick>")
def nick(nick):
    return f'bem vindo, seu nick é: {escape(nick)}'


@app.route('/login')
def login():
    return 'login'


@app.route("/<name>")

def hello(name):
    return f'bem vindo user {escape(name)}!'


if __name__== '__main__':
    app.run(debug=True)

@app.route('/admin/<adm>')
def admin(adm):

    if adm == "gerard":
        return redirect (url_for("login"))
    else:
       return  redirect (url_for('login'))

if __name__=='__main__':
    app.run(debug=True)



