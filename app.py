

from distutils.log import debug
from markupsafe import escape
from flask import Flask
from flask import url_for
from flask import redirect, url_for
from flask import render_template


app= Flask(__name__)


@app.route("/teste/<numb>")
def print(numb):
    return f'ola sua colisao sera em {numb}'
  

@app.route("/")
def menu():
    return render_template('index.html')
    

@app.route("/nick/<nick>")
def nick(nick):
    return f'bem vindo, seu nick é: {escape(nick)}'


@app.route('/menu', methods=['POST'])
def login():
    return render_template ('menu.html')


@app.route("/ida/<name>")
def hello(name):
    return f'bem vindo user {escape(name)}!'

if __name__=='__main__':
    app.run(debug=True)





