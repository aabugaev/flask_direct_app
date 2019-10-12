import requests, json
from flask import Flask, render_template, request, redirect, jsonify
app = Flask(__name__)

ID = ""
SECRET = ""

@app.route('/')
def direct_api():
	try:
		code = request.args.get('code')
		print(code)
		mydict = {"grant_type": "authorization_code", "code": code, "client_id" : ID, "client_secret": SECRET}
		req = requests.post("https://oauth.yandex.ru/token", data = mydict)
		print(req.text)
		token = req.json()["access_token"]
		print(req.json()["access_token"])
		
		CampaignsURL = 'https://api.direct.yandex.com/json/v5/campaigns'

		headers = {"Authorization": "Bearer " + token, "Accept-Language": "ru"}
		body = {"method": "get", "params": {"SelectionCriteria": {}, "FieldNames": ["Id", "Name","Funds"]}}
		jsonBody = json.dumps(body, ensure_ascii=False).encode('utf8')
		result = requests.post(CampaignsURL, jsonBody, headers=headers)
		print(result.text)
		
		return(result.text)

	except:
		print('=== no code ===')
	return render_template('my_template.html')

#@app.route('/result',methods = ['POST', 'GET'])
#def result():
#   if request.method == 'POST':
#      result = request.form
#      return redirect("https://oauth.yandex.ru/authorize?response_type=code&client_id="+ID)

if __name__ == '__main__':
   app.run(debug = True)