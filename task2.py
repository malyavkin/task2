from flask import Flask
app = Flask(__name__)
PORT = 5003


@app.route('n_prime')
def hello_world():
    return 'ok'

if __name__ == '__main__':
    app.run(port=PORT)
