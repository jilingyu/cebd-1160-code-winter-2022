import flask
import random

app = flask.Flask(__name__)
app.config["DEBUG"] = True

# Mapping here get->/, maps to the home() fcn.
@app.route('/', methods=['GET'])
def home():


	my_dataset = [{'id':0,'name':'The Title' }, {'id':1,'name':' Title2'}]

	return flask.jsonify(my_dataset)



	return_dict_list = []

	for x in range(100):
		rec = { 'id': x, 'age': random.randint(10,100) }
		return_dict_list.append(rec)

	return flask.jsonify(return_dict_list)
	# return "<h1>The Title of the Page</h1><p>This is some text on the Web Page.</p>"

app.run(host='0.0.0.0')
