import json
from flask import Flask, request, render_template
from markupsafe import escape

app= Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        form = dict(request.form)
        app.logger.info(f"{form}")
        return render_template('login.html')

    return render_template('login.html')


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





