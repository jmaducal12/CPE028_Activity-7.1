from flask import Flask, render_template, make_response
import requests
import pdfkit

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

@app.route('/export_pdf')
def export_pdf():
    ip_info = get_ip_info()

    if ip_info:
        rendered_html = render_template('pdf.html', ip_info=ip_info)
        config = pdfkit.configuration(wkhtmltopdf='/usr/bin/wkhtmltopdf')
        pdf = pdfkit.from_string(rendered_html, False, configuration=config)
        response = make_response(pdf)
        response.headers['Content-Disposition'] = 'attachment; filename=ip_info.pdf'
        response.headers['Content-type'] = 'application/pdf'
        return response

    return "Failed to retrieve."

if __name__ == "__main__":
    app.run (debug=True)

