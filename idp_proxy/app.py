import flask
from flask import request,jsonify,redirect
import requests
import os
import base64
from dotenv import load_dotenv
load_dotenv()
import urllib

app = flask.Flask(__name__)
app.secret_key = "secret_key"

CLIENT_ID = os.environ.get('CLIENT_ID')
CLIENT_SECRET = os.environ.get('CLIENT_SECRET')
IDP_BASE_URL = os.environ.get('IDP_BASE_URL')
REDIRECT_URI = 'http://localhost:5000'

@app.route('/')
def index():
	code = request.args.get('code')
	print(code)
	if code:
		byteData = f"{CLIENT_ID}:{CLIENT_SECRET}".encode('utf-8')
		encoded = base64.b64encode(byteData).decode('utf-8')
		token_url = f"{IDP_BASE_URL}/token"
		headers = {
			'Authorization': f"Basic {encoded}",
			'Content-Type': 'application/x-www-form-urlencoded'
		}
		data = {
			'grant_type': 'authorization_code',
			'code': code,
			'redirect_uri': REDIRECT_URI
		}

		print(token_url, headers, data)
		response = requests.post(token_url, headers=headers, data=data)
		print(response.json())
		if response.status_code == 200:
			token_data = response.json()
			access_token = token_data.get('access_token')
			refresh_token = token_data.get('refresh_token')
			token_type = token_data.get('token_type')
			expires_in = token_data.get('expires_in')
	
			userinfo_endpoint = f"{IDP_BASE_URL}/userinfo"
			headers = {'Authorization': f"{token_type} {access_token}"}
			userinfo_response = requests.get(userinfo_endpoint, headers=headers)
			userinfo = userinfo_response.json()
			email = userinfo.get('email')
	
			data = {
				'access_token': access_token,
				'refresh_token': refresh_token,
				'token_type': token_type,
				'expires_in': expires_in,
				'email': email
			}
	
			# redirect to localhost and put data in url 
			url = f"http://localhost:8080/auth/v1/idp?{urllib.parse.urlencode(data)}"
			return redirect(url)
		else:
			return jsonify({'message': 'Server error'}), 500

	return jsonify({'message': 'Invalid code'}), 400

if __name__ == '__main__':
	app.run(debug=True)