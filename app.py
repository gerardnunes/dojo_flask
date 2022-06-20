

import os
from pydoc import pipepager
from winreg import ExpandEnvironmentStrings
from flask import Flask, redirect, request, render_template, flash, url_for 
from markupsafe import escape

sql_email= []
sql_password= []

app= Flask(__name__)
app.secret_key = os.getenv('SECRET_KEY')

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():


    def users():
        form = dict(request.form)
        request.form['semail']
        request.form['spassword']
        sql_users={
            'user': request.form['semail'],
            'senha': request.form['spassword']

        }

    form = dict(request.form)
    if request.method == 'GET':
         return render_template('signup.html', context={})

    form = dict(request.form)
    error_message = validate_form_signup(form) # => error_message = 'Email é obrigatório' | 'Email não encontrado' | 'Senha inválida' | None
    if error_message:
        flash(error_message, 'danger')
        #usa no terminal os bag abaixo!! so pra testar mesmo





      
        sql_users={
            'user': request.form['semail'],
            'senha': request.form['spassword']

        }



        sql_password.append(request.form['spassword'])
        sql_email.append(request.form['semail'])



        
        return render_template('signup.html', context={'semail': form['semail']})

    flash(f"Seja bem-vindo, {form['semail']}!", 'success')
    return redirect(url_for('index'))



@app.route('/catalog',  methods=['GET', 'POST'])

def catalog():
    form = dict(request.form)

    
    if request.method == 'GET':
        return render_template('catalog.html')

    flash(f"Seja bem-vindo, {form['semail']}!", 'success')

    




def validate_form_signup(form):


    form = dict(request.form)


    

    if not form['semail'].endswith('@gmail.com'):
        return 'email precisa terminar em @gmail.com'
    
    if "@" and "*" not in form['spassword']:
        return 'senha nescessita de caracteres @, *' 

    
@app.route('/login', methods=['GET', 'POST'])

        

def login():


    if request.method == 'GET':
        return render_template('login.html', context={})

    form = dict(request.form)
    
    error_message =  validate_sql(form) # => error_message = 'Email é obrigatório' | 'Email não encontrado' | 'Senha inválida' | None
    if error_message:
        flash(error_message, 'danger')
        return render_template('login.html', context={'semail': form['semail']})

    flash(f"Seja bem-vindo, {form['semail']}!", 'success')
    return redirect(url_for('catalog'))




def validate_sql(form):

    sql_users= {
        'user': 'nalu@gmail.com',
        'senha': '5568@*',
        'user': 'gerard@gmail.com',
        'senha': '5568@*'

    }

    if not form['semail']:
        return 'email é obrigatorio'

    if form['semail'] != 'nalu@gmail.com' and 'gerard@gmail.com': 
        return 'email nao encontrado, ja fez o nosso cadrasto?'

    if form['spassword'] != '5568@*':
        return 'senha invalida.'


# def login(): v2
#     if request.method == 'GET':
#         return render_template('login.html', context={})

#     form = dict(request.form)

#     if not form['email']:
#         return return_invalid_login(form['email'], 'Email é obrigatório')
    
#     if form['email'] != 'gerard@email':
#         return return_invalid_login(form['email'], 'Email não encontrado')

#     if form['password'] != '123456':
#         return return_invalid_login(form['email'], 'senha invalida')

#     flash(f"Seja bem-vindo, {form['email']}!", 'success')
#     return redirect(url_for('index'))

# def return_invalid_login(email, message):
#     flash(message, 'danger')
#     return render_template('login.html', context={'email': email})

# def login(): v1
#     erro = None
#     if request.method == 'POST':
#         if request.form["email"] != 'gerard@email' or \
#                 request.form['password'] != '123456':
#                 error = 'senha ou email errada'
#         else:
#                 form = dict(request.form)
#                 app.logger.info(f'{form}')
#                 flash( f"voce esta conectado como usuario '{form['email']}'" , 'info')
#                 return redirect(url_for('login'))
                
#         form = dict(request.form)
#         app.logger.info(f"{form}")
#         flash(f"Usuário '{form['email']}' não encontrado", 'danger')
#         context = {'email': form['email']}
#         return render_template('login.html', context=context)

#     return render_template('login.html', context={})


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










