from flask import Flask
from flask import render_template
from flask import request
import sys
import optparse
import time


app = Flask(__name__)

start = int(round(time.time()))

@app.route('/')
def hello():
    return render_template ("Choosing_Service.html") 

@app.route('/RU',methods=['GET', 'POST'])
def RU():
	if request.method == 'GET':
		return render_template ("Choosing_Server.html")  
	elif request.method == 'POST':
		RackUnit=request.form['submittedAnswer'];
		if RackUnit == '1':
			return "You need a C220M4";
		elif RackUnit == '2':
			return "You need a C240M4";
		elif RackUnit == '4':
			return "<a href=http://www.cisco.com/c/dam/en/us/products/collateral/servers-unified-computing/ucs-c-series-rack-servers/c460m4_specsheet.pdf>You need a C40M4, Spec sheet here!</a>"

@app.route('/CPU',methods=['GET', 'POST'])
def CPU():
	if request.method == 'GET':
		return render_template ("Choosing_CPU.html.html")  
	elif request.method == 'POST':
		Proc=request.form['submittedAnswer'];
		if Proc == 'E5':
			return "You need a C220M4";
		elif Proc == 'E72':
			return "You need a C240M4";
		elif Proc == 'E73':
			return "C460"

@app.route('/Memory',methods=['GET', 'POST'])
def Memory():
	if request.method == 'GET':
		return render_template ("Choosing_Memory.html")  
	elif request.method == 'POST':
		Mem=request.form['submittedAnswer'];
		if Mem == 'Small':
			return "You need a C220M4 or C240M4";
		elif Mem == 'Large':
			return "You can get up to 6TB with the C460M4";

if __name__ == '__main__':
    parser = optparse.OptionParser(usage="python routes.py -p ")
    parser.add_option('-p', '--port', action='store', dest='port', help='The port to listen on.')
    (args, _) = parser.parse_args()
    if args.port == None:
        print ("Missing required argument: -p/--port")
        sys.exit(1)
    app.run(host='0.0.0.0', port=int(args.port), debug=False)