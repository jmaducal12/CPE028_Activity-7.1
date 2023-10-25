from flask import Flask, render_template
import requests

app = Flask(__name__)

API_URL = 'https://ipapi.co/json/'

def get_ip_info():
    response = requests.get(API_URL)

    if response.status_code == 200:
        return response.json()
    else:
        return None

@app.route('/')
def index():
    ip_info = get_ip_info()
    return render_template('index.html', ip_info=ip_info)

if __name__ == "__main__":
    app.run (debug=True)

