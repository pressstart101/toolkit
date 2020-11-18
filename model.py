from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()

class User(db.Model):
    """Feline catus."""

    __tablename__ = "users"

    user_id = db.Column(db.Integer,
                       primary_key=True,
                       autoincrement=True,
                       )
    email = db.Column(db.String(50), nullable=False, unique=True,)
    password = db.Column(db.String(50), nullable=False,)

class Report(db.Model):
    """Feline catus."""
    def __init__(self, **details):
        self.url = details['url']
        self.is_vulnerable = details['is_vulnerable']
        self.exploit = details.get("exploit")
        self.field_name = details.get('field_name')
        self.method = details.get('method')
        self.form_type = details.get('form_type')


    __tablename__ = "reports"
    report_id = db.Column(db.Integer,
                       primary_key=True,
                       autoincrement=True,
                       )
    url = db.Column(db.String(100), nullable=False)
    exploit = db.Column(db.String(100))
    form_type = db.Column(db.String(50))
    field_name = db.Column(db.String(50))
    is_vulnerable = db.Column(db.String(50), nullable=False,)
    method = db.Column(db.String(50))


def connect_to_db(app):
    """Connect the database to our Flask app."""

    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres:///users'
    app.config['SQLALCHEMY_ECHO'] = False
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.app = app
    db.init_app(app)









if __name__ == '__main__':
    from server import app

    # As a convenience, if we run this module interactively, it will leave
    # you in a state of being able to work with the database directly.
    connect_to_db(app)
    print('Connected to db!')