from flask_security import Security, SQLAlchemyUserDatastore, \
    UserMixin, RoleMixin, login_required

class UserDatastore(object):

    def __init__(self, db):
        self.db = db
        self.set_roles_users(db)
        self.set_role(db)
        self.set_user(db)
        self.set_user_datastore(db)

    def set_user_datastore(self, db):
        self.user_datastore = SQLAlchemyUserDatastore(db, self.User, self.Role)

    def set_roles_users(self, db):
        self.roles_users = db.Table('roles_users',
            db.Column('user_id', db.Integer(), db.ForeignKey('user.id')),
            db.Column('role_id', db.Integer(), db.ForeignKey('role.id')))

    def set_role(self, db):
        class Role(db.Model, RoleMixin):
            id = db.Column(db.Integer(), primary_key=True)
            name = db.Column(db.String(80), unique=True)
            description = db.Column(db.String(255))
        self.Role = Role

    def set_user(self, db):
        class User(db.Model, UserMixin):
            id = db.Column(db.Integer, primary_key=True)
            email = db.Column(db.String(255), unique=True)
            password = db.Column(db.String(255))
            active = db.Column(db.Boolean())
            confirmed_at = db.Column(db.DateTime())
            roles = db.relationship('Role', secondary=self.roles_users,
                                    backref=db.backref('users',
                                    lazy='dynamic'))

        self.User = User
