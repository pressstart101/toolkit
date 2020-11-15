from flask import Flask, render_template, request, flash, session,redirect, jsonify, session
from flask import send_from_directory
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from seed_ping import kickoff_tcpdump, test_ping, PingListener
from model import connect_to_db, User
import crud
import os
import time
from xss import XSS
import pdb 
from config import SECRET_KEY



app = Flask(__name__)
app.config['SECRET_KEY'] = SECRET_KEY



@app.route('/login', methods=['GET','POST'])
def login():
    # pdb.set_trace()
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        user = crud.get_user_by_email(email)
        if user == None:
            flash("Doesnt exist!")
            return redirect('/login')    

        elif user.password == password:
            session['logged_in_as'] = user.user_id

            flash("Logged in!")
            return redirect('/')

        else:
            flash("you fake")
            return redirect('/login')

    return render_template('/login.html')






    """Log user into application."""
    # if request.method == 'POST':
    #     session['email'] = request.form['email']
    #     session['password'] = request.form['password']

    # # email = request.form['email']
    # # password = request.form['password']

    # if session['password'] == 'let-me-in':   
    #     session['current_user'] = email
    #     flash(f'Logged in as {email}')
    #     return redirect('/')

    # else:
    #     flash('Wrong password!')
    #     return redirect('/login')


@app.route('/')
def homepage():
    """View homepage."""
    session['user'] = "email"
    return render_template('homepage.html')

# @app.route('/login')
# def login():
#     print('works')
#     return render_template('login.html')


@app.route('/api/ping.json')
def ping():

    
    # ping.get_pings()
    # time.sleep(5)
    # ping.get_pings()

    

    time.sleep(3)
    p = ping_init.get_pings()



    # print('before')
    # print(p)
    # print('after')
    # ping = kickoff_tcpdump()
    # print(ping)
    # print(type(ping))

    # no_pings = {"pings": None}
    return jsonify(p)
    # return jsonify(no_pings)



@app.route('/api/xss.json')
def xss_test():
    xss = XSS()
    # url = "https://xss-game.appspot.com/level1/frame"
    url = request.args["url_form"]
    print("this is url \n\n\n")
    print(url)

    print("done\n\n\n")
    xss = XSS()
    result = xss.scan_xss(url)
    print("result\n\n\n")
    print(result)
    print(xss.scan_xss(url))
    # print(xss.scan_xss(url))
    # return jsonify(xss)
    return jsonify(result)
# @app.route('/favicon.ico')
# def favicon():
#     return send_from_directory(os.path.join(app.root_path, 'static/img'),
#                           'favicon.ico')

@app.route('/api/user/<int:user_id>')
def get_user(user_id):
    """Return a user from the database as JSON."""

    user = User.query.get(user_id)

    if user:
        return jsonify({'status': 'success',
                        'user_id': user.user_id,
                        'email': user.email,
                        'password': user.password})
    else:
        return jsonify({'status': 'error',
                        'message': 'No user found with that ID'})

if __name__ == '__main__':
    connect_to_db(app)
    global ping_init
    ping_init = PingListener()
    ping_init.start_listening()


    
    app.run(host='0.0.0.0', debug=True, threaded=True)   