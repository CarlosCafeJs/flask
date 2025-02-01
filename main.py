from flask import Flask, render_template, request, redirect, session, flash, url_for

class Jogo:
    def __init__(self, nome, categoria, console): 
        self.nome=nome
        self.categoria=categoria
        self.console=console

jogoUm = Jogo('Tetrix', 'Pyzzle', 'Atari')
jogoDois = Jogo('Call of Duty', 'FPS', 'PC')
jogoTres = Jogo('Warface', 'Firt Person', 'PC')
lista = [jogoUm, jogoDois, jogoTres]

app = Flask(__name__)
app.secret_key = 'TesteMaior'

class Usuario:
    def __init__(self, nome, nickname, senha):
        self.nome=nome
        self.nickname=nickname
        self.senha=senha

usuarioUm = Usuario("Carlos", "carloscafe", "Ckarlos36")
usuarioDois = Usuario("Thaylon", "enzo", "1234")
usuarioTres = Usuario("Bia", "bix", "12345")

usuarios = {   
    usuarioUm.nickname : usuarioUm,
    usuarioDois.nickname : usuarioDois,
    usuarioTres.nickname : usuarioTres
}

@app.route('/')
def index():
    # lista = ['Tetrix', 'Call of Duty', 'Warface']
    if 'usuario_logado' not in session or session['usuario_logado'] == None:
        return redirect(url_for('login'))
    else:
        return render_template('index.html', titulo='jogos', jogos=lista)

@app.route('/novo')
def novo():
    if 'usuario_logado' not in session or session['usuario_logado'] == None:
        return redirect(url_for('login', proxima=url_for('novo')))
    else:
        return render_template('novo.html', titulo='Adicione um novo Jogo :')


@app.route('/criar', methods=['POST',])
def criar():
    nome = request.form['nome'] 
    categoria = request.form['categoria'] 
    console = request.form['console'] 
    jogo = Jogo(nome, categoria, console)
    lista.append(jogo)    
    return redirect(url_for('index'))


@app.route('/login')
def login():   
    proxima = request.args.get('proxima')
    return render_template('login.html', titulo='Login', proxima=proxima)


@app.route('/autenticar', methods=['POST', ])
def autenticar():
    if request.form['usuario'] in usuarios:
        usuario = usuarios[request.form['usuario']]
        if request.form['senha'] == usuario.senha:
            session['usuario_logado'] = usuario.nickname
            flash(usuario.nickname + ' logado com sucesso!')
            proxima_pagina = request.form['proxima']
            return redirect(proxima_pagina)
        else:
            flash('Usuário não logado.')
            return redirect(url_for('login'))


@app.route('/logout')
def logout():
    session['usuario_logado'] = None
    flash('Logout efetuado com sucesso!')
    return redirect(url_for('login'))




app.run(debug=True, host='0.0.0.0', port=8080)