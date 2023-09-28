from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    title = 'MOBVAP'
    return render_template('home.html', title = title)

@app.route("/regulamento")
def regulamento():
    title = 'Regulamento - MOBVAP'
    return render_template('regulamento.html', title = title)

@app.route("/registros")
def registros():
    title = 'Registros - MOBVAP'
    return render_template('registros.html', title = title)

if __name__ == '__main__':
    app.run()