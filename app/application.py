from flask import Flask, render_template, request
import json
import bias_checker
import extract_SVOs




app = Flask(__name__)


@app.route("/")
def index():
	return render_template("index.html")

@app.route("/api/bias-checker", methods=['POST', 'GET'])
def handle():
	q = request.args.get('query', type=str)
	sentence = str(request.form['query'])
	print(sentence)
	biased = bias_checker.check_for_bias(sentence)
	print(bias_checker.output(biased))
	resp = bias_checker.output(biased)
	return resp


if __name__ == '__main__':
   app.run(debug = True)