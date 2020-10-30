from flask import Flask, render_template, request, flash, session,redirect, jsonify
from flask import send_from_directory
from seed_ping import kickoff_tcpdump, test_ping
import crud
import os



app = Flask(__name__)



@app.route('/')
def homepage():
    """View homepage."""
    return render_template('homepage.html')


@app.route('/api/ping.json')
def ping():
    ping = test_ping()
    # ping = kickoff_tcpdump()
    # print(ping)
    # print(type(ping))
    return jsonify(ping)


# @app.route('/favicon.ico')
# def favicon():
#     return send_from_directory(os.path.join(app.root_path, 'static/img'),
#                           'favicon.ico')



if __name__ == '__main__':
    # connect_to_db(app)
    app.run(host='0.0.0.0', debug=True)   