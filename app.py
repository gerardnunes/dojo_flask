import os
from flask import Flask, redirect, request, render_template, flash, url_for 
from markupsafe import escape

app= Flask(__name__)
app.secret_key = os.getenv('SECRET_KEY')

@app.route("/")
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        form = dict(request.form)
        app.logger.info(f"{form}")
        flash(f"Usuário '{form['email']}' não encontrado", 'danger')
        context = {'email': form['email']}
        return render_template('login.html', context=context)


    return render_template('login.html', context={})


@app.route("/teste/<numb>")
def print(numb):
    return f'ola sua colisao sera em {numb}'

@app.route("/nick/<nick>")
def nick(nick):
    return f'bem vindo, seu nick é: {escape(nick)}'

@app.route("/ida/<name>")
def hello(name):
    return f'bem vindo user {escape(name)}!'

if __name__=='__main__':
    app.run(debug=True)





