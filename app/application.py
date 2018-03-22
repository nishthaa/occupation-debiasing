from flask import Flask, render_template, request, jsonify
import json
import bias_checker
import extract_SVOs


def is_occupation(occ):
	fh = open("data/result.txt")
	for line in fh:
		toks = line.split(",")
		words = [tok.strip().lower() for tok in toks]
		if words[0] == occ.lower().strip():
			fh.close()
			return words[2]
	fh.close()
	return False


app = Flask(__name__)


@app.route("/")
def home():
	return render_template("home.html")

@app.route("/index.html")
def demo():
	return render_template("index.html")

@app.route("/api/bias-checker", methods=['POST', 'GET'])
def handle():
	#print(request.form['query'])
	tf = int(request.form['from'])
	tt = int(request.form['to'])
	country = str(request.form['place'])
	#print(tf, tt, country)
	sentence = str(request.form['query'])
	#print(sentence)
	biased, triplets = bias_checker.check_for_bias(sentence)
	occ_triplets = [trp for trp in triplets if is_occupation(trp[2])]
	for i in range(len(occ_triplets)):
		occ_triplets[i] = (occ_triplets[i][0].capitalize(), occ_triplets[i][1], occ_triplets[i][2])
	#print(bias_checker.output(biased, tf, tt, country))
	resp = bias_checker.output(biased, tf, tt, country)
	return jsonify(response=[resp, occ_triplets])


if __name__ == '__main__':
   app.run(debug = True)