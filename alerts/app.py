from flask import Flask, request, json
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/robusta-alerts",methods=['POST'])
def alerts():
  if request.method == 'POST':
    print('Webhook Received')
    #request_json = request.get_json()
    request_data = request.data

    print('Payload: ')
    print(request_data)
    #print(json.dumps(request_json,indent=4))
    return 'Webhook notification received', 202
  else:
    return 'POST Method not supported', 405
    

if __name__ == '__main__':
    app.run()
