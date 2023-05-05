from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/switchOn', methods=['POST'])
def switchOn():
    
    url = "http://192.168.178.188/cm?cmnd=Power%20On"
    response = requests.get(url)
    return response.text

@app.route('/switchOff', methods=['POST'])
def switchOff():
    
    url = "http://192.168.178.188/cm?cmnd=Power%20Off"
    response = requests.get(url)
    return response.text
   
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
