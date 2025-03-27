from flask import Flask
from data import db_session
from data.users import User

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


def main():
    db_session.global_init("db/blogs.db")
    user = [
        User(surname='Scott', name='Ridley', age=21,
             position='captain', speciality='research engineer',
             address='module_1', email='scott_chief@mars.org'),

        User(surname='Murkinez', name='Dai', age=16,
             position='captain', speciality='ml engineer',
             address='module_3', email='davmrkinez@mars.org'),

        User(surname='Rock', name='Skala', age=99,
             position='Rock', speciality='Real rock',
             address='module_99', email='rock@mars.org')]

    db_sess = db_session.create_session()
    db_sess.add_all(user)
    db_sess.commit()


if __name__ == '__main__':
    main()