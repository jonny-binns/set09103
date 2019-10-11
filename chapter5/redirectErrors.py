from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
	return "hello napier"

@app.errorhandler(404)
def page_not_found(error):
	return "couldn't find the reuqested page", 404

if __name__ == "__main__":
	app.run(host='0.0.0.0', debug=True)

