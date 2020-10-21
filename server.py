from flask import Flask, render_template, request, flash, session,redirect, jsonify
from seed_ping import kickoff_tcpdump, test_ping
import crud


app = Flask(__name__)



@app.route('/')
def homepage():
    """View homepage."""
    return render_template('homepage.html')


@app.route('/api/ping.json')
def ping():
    ping = test_ping()
    # ping = kickoff_tcpdump()
    print(ping)
    print(type(ping))
    return jsonify(ping)






if __name__ == '__main__':
    # connect_to_db(app)
    app.run(host='0.0.0.0', debug=True)   