from flask import Flask, render_template, request, flash, session,redirect, jsonify, session, get_flashed_messages
from flask import send_from_directory, send_file
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from seed_ping import kickoff_tcpdump, test_ping, PingListener
from model import connect_to_db, User
from model import Report
import crud
import os
import time
from xss import XSS
import pdb 
from config import SECRET_KEY
import jinja2
import json
import urllib.parse



app = Flask(__name__)
app.config['SECRET_KEY'] = SECRET_KEY


result = {}

@app.route('/login', methods=['GET','POST'])
def login():
    print("\n\n flash messages")
    print(get_flashed_messages())
    # pdb.set_trace()
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        user = crud.get_user_by_email(email)
        if user == None:
            flash("User doesnt exist")
            return redirect('/login')    

        elif user.password == password:
            session['logged_in_as'] = user.user_id

            # flash("Logged in!")
            return redirect('/')

        else:
            flash("you fake")
            return redirect('/login')

    return render_template('/login.html')


@app.route('/logout')
def logout():
    if "logged_in_as" in session:
        user = session['logged_in_as']
        flash('you have been logged out', 'info')
    session.pop('logged_in_as', 'none')
    
    return redirect('/login')

# position absolute

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
    # session['user'] = "email"
    if session.get('logged_in_as'):
        user = crud.get_user_by_id(session['logged_in_as'])
        # flash(f'Welcome back, {user.email}')
        session['user'] = user.email
    else:
        return redirect('/login')
    return render_template('homepage.html')


@app.route('/reports')
def reports():
    print('hi\n')
    reports = crud.return_all_reports()
    print(reports[0].url)
    print('after')
    return render_template("reports.html", reports=reports)


@app.route('/search')
def search():
    query = request.args.get('query')
    print(query)
    print("THIS IS QUERY\n\n\n")
    # reports = Report.query.search(query, limit=num_posts)
    # reports = Report.query.filter_by(query, limit=num_posts)
    if query:
        reports = crud.search_reports(query)

    print(f'\n\n\n\n\REPORTS{reports}n\n\n\n\n')
    # reports = crud.return_all_reports()
    # reports = Report.query.search(query, limit=num_posts).all()


    return render_template('reports.html', reports=reports)
    # return render_template('reports.html')


    # searchForm = searchForm()
    # reports = Report.query

    # if searchForm.validate_on_submit():
    #     reports = reports.filter(models.Report.url.like('%' + searchForm.report.data + '%'))

    # reports = reports.order_by(Report.name).all()

    return render_template('reports.html', reports = reports)

@app.route('/save_report')
def save_report():
    print(f'\n\n\n\nTHIS IS REPORT {result}\n\n\n\n\n')
    print(f'\n\n\n\nFROM SAVE_REPORT \n\n\n')
    # url = result['url']
    # is_vulnerable = result['is_vulnerable']
    # if result['is_vulnerable'] == False:
    #     crud.create_report(url, is_vulnerable)
    # else:
    #     exploit = result['exploit']
    #     field_name = result['field_name']
    #     form_type = result['form_type']
    #     method = result['method']

    #     crud.create_report(url, is_vulnerable, exploit, field_name, form_type, method)
    if crud.create_report(result):
        flash('report saved!')  
    else:
        flash("couldn't save the report")     
    return render_template('homepage.html')

# @app.route('/flash_for_save_report')
# def flash_msg():
#     flash('report successfully saved')

# @app.route('/flash_for_scanning')
# def flash_msg():
#     flash('scanning...')
    

@app.route('/export')
def export():

    print('got here')
    # with open('dump.csv', 'wb') as f:
    #     out = csv.writer(f)
    #     out.writerow(['id', 'url'])

    #     for item in session.query(Report).all():
    #         out.writerow([report.id, report.url])

    # reports = crud.return_all_reports()
    # pickle_out = open("outfile", "w")
    # for report in reports:
    #     # pickle.dump(report, pickle_out)
    #     pickle_out.write(report)

    # pickle_out = open('outfile', 'wb')
    # pickle.dump(report, pickle_out)

    # serialized = pickle.load(report)
    # print(f'\n\n\nReport {serialized}')
    # file = open('reports', 'w')
    # file.write(report)
    # file.close()


    reports = session.get('reports', None)
    # df = pandas.read_json(reports)
    # result = df.to_csv()

    with open('outfile', 'w') as fout:
        json.dump(reports, fout)

    return jsonify(reports)
    # print(f'\n\n\n{result}\n\n\n')
    # return send_file('/home/vagrant/src/project/outfile',  attachment_filename="reports.json") 



@app.route('/api/reports.json')
def get_reports():
    result = []
    reports = crud.return_all_reports()
    for report in reports:
        obj = {'url': report.url, 'is_vulnerable': report.is_vulnerable, 'successful_payload': report.exploit, 'vulnerable_filed_name_tag': report.field_name, 'vulnerable_form_type': report.form_type, 'method': report.method}
        result.append(obj)
        session['reports'] = result
        print(session['reports'])

    


    return jsonify(result)

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
    # flash("scanning...")
    xss = XSS()
    # url = "https://xss-game.appspot.com/level1/frame"
    url = request.args["url_form"]
    print("this is url \n\n\n")
    print(url)
    
    print("done\n\n\n")
    xss = XSS()
    global result
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


@app.route('/urlcode')
def encode(encodedStr):
    return urllib.parse.quote_plus(encodedStr)

def decode(encodedStr):
    return urllib.parse.unquote(encodedStr)



@app.route('/users', methods=['POST']) 
def register_user():
    email = request.form.get('email')
    password = request.form.get('password')
    if crud.get_user_by_email(email) == None:
        user = crud.create_user(email, password)
        flash("Account Created Successfully")
        return redirect('/')
    else:
        flash("User already exists")
        return redirect("/")

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



   

    
    # app.run(host='0.0.0.0', debug=True, threaded=True) 
    app.run(host='0.0.0.0', threaded=True)   