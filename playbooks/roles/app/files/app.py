from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route('/')
def index():
    # Fetch AWS IP Ranges
    response = requests.get('https://ip-ranges.amazonaws.com/ip-ranges.json')
    data = response.json()

    # Filter Route53 and S3 ranges
    services = ['ROUTE53_HEALTHCHECKS', 'S3']
    filtered = [entry for entry in data['prefixes'] if entry['service'] in services]

    # Sort data by service
    filtered.sort(key=lambda x: x['service'])

    # Render table
    return render_template('index.html', ip_ranges=filtered)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
