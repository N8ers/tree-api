from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return 'Welcom to the Tree API!'


if __name__ == '__main__':
    app.run(debug=True)
