from flask import Flask
app = Flask(__name__)

@app.route("/")
def root():
	return "the default, 'root' route"

@app.route("/hello/")
def hello():
	return "Hello Napier"

@app.route("/goodbye/")
def goodbye():
	return "Goodbye Napier"

if __name__ == "__main__":
	app.run(host='0.0.0.0', debug=ture)
