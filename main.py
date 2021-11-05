import socket
from flask import Flask, request ,jsonify,make_response

app = Flask(__name__)

@app.route('/', methods=['GET'])
def return_hostname():
     sucess = 200
     return jsonify("sucess:True", " hostname   : {} ".format(socket.gethostname()))

if __name__ == '__main__':
	app.run(host="0.0.0.0", debug=True)
