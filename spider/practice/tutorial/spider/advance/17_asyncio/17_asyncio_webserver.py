import time

from flask import Flask

app = Flask(__name__)


@app.route('/bobo')
def index_bobo():
    time.sleep(2)
    return 'hello bobo'


@app.route('/jay')
def index_jay():
    time.sleep(2)
    return 'hello jay'


@app.route('/vikingar')
def index_vikingar():
    time.sleep(2)
    return 'hello vikingar'


if __name__ == '__main__':
    app.run(threaded=True)
