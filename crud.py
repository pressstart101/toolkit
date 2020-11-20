from model import db, User, connect_to_db, Report


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




# def create_report(url, is_vulnerable, exploit=None, field_name=None, form_type=None, method=None):
#     """Create and return a new user."""
#     if is_vulnerable == False:
#         report = Report(url, is_vulnerable)
#     else:
#         report = Report(url, is_vulnerable, exploit, field_name, form_type, method)

#     db.session.add(report)
#     db.session.commit()
#     return Report.query.filter_by(url=url).first()


def create_report(result):
    """Create and return a new user."""
    url=result['url']
    is_vulnerable = result['is_vulnerable']
    if is_vulnerable == False:
        report = Report(url=url, is_vulnerable=is_vulnerable)
    else:
        url=result['url']
        result['is_vulnerable']
        exploit = result['exploit']
        field_name = result['field_name']
        form_type = result['form_type']
        method = result['method']

        report = Report(url=url, is_vulnerable=is_vulnerable, exploit=exploit, field_name=field_name, form_type=form_type, method=method)

    db.session.add(report)
    db.session.commit()
    return Report.query.filter_by(url=url).first()

def return_all_reports():
    return Report.query.all()
