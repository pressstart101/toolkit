from model import db, User, connect_to_db


if __name__ == '__main__':
    from server import app
    connect_to_db(app)


def create_user(email, password):
    """Create and return a new user."""

    user = User(email=email, password=password)

    db.session.add(user)
    db.session.commit()
    return user


def get_user_by_id(user_id):
    return User.query.get(user_id)    

def get_user_by_email(email):
    return User.query.filter_by(email=email).first()

