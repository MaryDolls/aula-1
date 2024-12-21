from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Rota 1 - Página Inicial (Apresentação Pessoal)
@app.route('/')
def index():
    return render_template('index.html')

# Rota 2 - Página de Contato
@app.route('/contato', methods=['GET', 'POST'])
def contato():
    if request.method == 'POST':
        return redirect(url_for('sucesso'))
    return render_template('contato.html')

# Rota 3 - Página de Confirmação
@app.route('/sucesso')
def sucesso():
    return render_template('sucesso.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)