from flask import Flask, render_template, request, flash, session,redirect, jsonify
from flask import send_from_directory
from seed_ping import kickoff_tcpdump, test_ping, PingListener
import crud
import os
import time
from xss import XSS




app = Flask(__name__)



@app.route('/')
def homepage():
    """View homepage."""
    return render_template('homepage.html')


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
    return jsonify(p)



@app.route('/api/xss.json')
def xss_test():
    xss = XSS()
    url = "https://xss-game.appspot.com/level1/frame"
    print(xss.scan_xss(url))
    return jsonify(xss)
# @app.route('/favicon.ico')
# def favicon():
#     return send_from_directory(os.path.join(app.root_path, 'static/img'),
#                           'favicon.ico')



if __name__ == '__main__':
    # connect_to_db(app)
    global ping_init
    ping_init = PingListener()
    ping_init.start_listening()
    # xss = XSS()
    # url = "https://xss-game.appspot.com/level1/frame"
    # print(xss.scan_xss(url))
    app.run(host='0.0.0.0', debug=True, threaded=True)   