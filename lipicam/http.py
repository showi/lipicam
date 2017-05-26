from flask import Flask, Response, render_template
import flask
import flask_login
from flask_sqlalchemy import SQLAlchemy
from flask_security import Security, SQLAlchemyUserDatastore, \
    UserMixin, RoleMixin, login_required
from lipicam.cam import Cam
from lipicam.config import config
from lipicam import util
from lipicam import log

cam = Cam()
app = Flask(__name__)
app.config['SECRET_KEY'] = util.gen_secret()
sqluri = 'sqlite:///{}/userdb'.format(config.getpath('config', 'user'))
log.debug('SqlUri: {}'.format(sqluri))
app.config['SQLALCHEMY_DATABASE_URI'] = sqluri
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
from lipicam import user
UDS = user.UserDatastore(db)
user_datastore = UDS.user_datastore
security = Security(app, user_datastore)

@app.before_first_request
def create_user():
    db.create_all()
    try:
        user_datastore.create_user(email='lipi', password='picam')
        db.session.commit()
    except Exception as e:
        log.error('CreateUserError: {}'.format(e))


@app.route('/')
@login_required
def main(name=None):
    return render_template('main.html.j2')

@app.route('/cam/stream')
@login_required
def route_cam_stream():
    return Response(cam.read(), mimetype='image/jpeg')


@app.route('/cam')
@login_required
def route_cam():
    return render_template('cam.html.j2')

def run():
    app.run(host=config.get('httpd', 'host'),
            port=config.getint('httpd', 'port'),
            debug=config.getboolean('main', 'debug'))

if __name__ == "__main__":
    run()
