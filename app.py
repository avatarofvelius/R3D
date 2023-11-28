
from flask import Flask, render_template

app = Flask(__name__)

if __name__ == '__main__':
    app.run('0.0.0.0', 5000)

## Index Route
@app.route('/')
def index():
    return render_template('index.html')

## Pico.css Route
@app.route('/pico')
def pico():
    return render_template('pico_index.html')

## Pico.css Route
@app.route('/pico_splash')
def pico_splash():
    return render_template('pico_splash.html')