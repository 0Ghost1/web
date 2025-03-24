from flask import Flask, render_template, request


app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'

@app.route('/')
@app.route('/index/<title>')
def index(title='Миссия Колонизация Марса'):
    return render_template('base.html', title=title)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')