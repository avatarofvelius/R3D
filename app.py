from flask import Flask, render_template

# Last Modified Date
import os
import datetime
file_path = 'templates/pico_index.html'
file_stat = os.stat(file_path)
modification_timestamp = file_stat.st_mtime
md = datetime.datetime.fromtimestamp(modification_timestamp)
# End 

app = Flask(__name__)

if __name__ == '__main__':
    app.run('0.0.0.0', 5000)

## Index Route
@app.route('/')
def index():
    return render_template('pico_index.html', md=md)

## Showcase
@app.route('/showcase')
def showcase():
    return render_template('pico_showcase.html', md=md)

## Pico.css Route
@app.route('/splash')
def splash():
    return render_template('pico_splash.html', md=md)

@app.route('/example')
def example():
    return render_template('example.html', md=md)