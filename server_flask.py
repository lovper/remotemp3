import _main
from flask import Flask
from flask import render_template

app = Flask(__name__)

with open('config.ini', "r") as f:
    if f.mode == 'r':
        for line in f:
            exec(line)
    else:
        print('Error reading settings')


main = _main.Main(dir)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/inp/<state>')
def inp(state=''):
    print(main.inp(state))
    return render_template('index.html', state=state)


if __name__ == '__main__':
    app.run()
