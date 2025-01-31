from flask import Flask, render_template, request, redirect

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
@app.route('/')
def index():
    # lista = ['Tetrix', 'Call of Duty', 'Warface']
    return render_template('index.html', titulo='jogos', jogos=lista)

@app.route('/novo')
def novo():
    return render_template('novo.html', titulo='Adicione um novo Jogo :')

@app.route('/criar', methods=['POST',])
def criar():
    nome = request.form['nome'] 
    categoria = request.form['categoria'] 
    console = request.form['console'] 
    jogo = Jogo(nome, categoria, console)
    lista.append(jogo)    
    return redirect('/')


@app.route('/login')
def login():    
    return render_template('login.html', titulo='Login')





app.run(debug=True, host='0.0.0.0', port=8080)