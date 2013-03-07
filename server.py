# http://neuralensemble.org/trac/sumatra/browser/src/recordstore/http_store.py
# /                                            GET
# /<project_name>/[?tags=<tag1>,<tag2>,...]    GET
# /<project_name>/tag/<tag>/                   GET, DELETE
# /<project_name>/<record_label>/              GET, PUT, DELETE
# and should both accept and return JSON-encoded data when the Accept header is
# "application/json".
# The required JSON structure can be seen in recordstore.serialization:
# http://neuralensemble.org/trac/sumatra/browser/src/recordstore/serialization.py
import os
from flask import Flask, request, render_template, jsonify, Response, send_file

app = Flask(__name__)
app.config.from_object(__name__)  
#app.config.from_pyfile('config.py')

# 'Content-Type': 'application/json'

@app.route("/")
def index():
	return jsonify({})

@app.route("/<string:project_name>/")
def get_project(project_name):
	return jsonify({})

@app.route("/<string:project_name>/tag/<string:tag>/", methods=('GET', 'DELETE'))
def project_tag(project_name, tag):
	return jsonify({})

@app.route("/<string:project_name>/<string:record_label>/", methods=('GET', 'DELETE', 'PUT'))
def project_label(project_name, record_label):
	print request.method
	if request.method == 'PUT':
		print request.data
	return jsonify({})

if __name__ == '__main__':
	# Bind to PORT if defined, otherwise default to 5000.
	port = int(os.environ.get('PORT', 5000))
	app.run(host='0.0.0.0', port=port, debug=app.debug)
