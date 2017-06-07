from flask import Flask, render_template, json, jsonify, request, Response, make_response, abort, url_for
import tsearch
import reddit
from time import gmtime, strftime

app = Flask(__name__)

likey = [
	{
		'id': 1,
		'title': u'Like',
		'description': u'Stuff, Junk, Things',
		'time': u'',
		'done': False
	}

]


#-- Index Page 
@app.route("/")
def main():
	return render_template('index.html')

#-- Get all likes

@app.route('/restful/api/likey', methods=['GET'])
def get_all():
	return jsonify({'likey': likey})

#-- POST
@app.route('/restful/api/likey', methods=['POST'])
def add_like():
	now = strftime("%Y-%m-%d %H:%M:%S", gmtime())
	if not request.json or not 'description' in request.json:
		abort(400)
	like = {
		'id': likey[-1]['id'] +1,
		'title': request.json.get('title',"like"),
		'description': request.json['description'],
		'time': now,
		'done': False
	}

	likey.append(like)
	return jsonify({'like': like}), 201

@app.route('/submit', methods=['POST'])
def submit():
	now = strftime("%Y-%m-%d %H:%M:%S", gmtime())
	likeSub = request.form['_like']
	likej = '"description":"' + likeSub + '"'
	like = {
		'id': likey[-1]['id'] +1,
		'title': 'Like',
		'description': likeSub,
		'time': now,
		'done': False
	}
	likey.append(like)
	return render_template('likedash.html', like=likeSub, hashtags=tsearch.hashy(likeSub), reddit=reddit.reddit(likeSub) )


@app.route('/likeDash')
def likeDash():
	return render_template('likedash.html')

#-- Error Handling
@app.errorhandler(404)
def not_found(error):
	return make_response(jsonify({'error': 'Not found'}), 404)

if __name__ == "__main__":
	app.run(debug=True)