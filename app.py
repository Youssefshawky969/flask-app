from prometheus_client import Counter, generate_latest
from flask import Flask, Response

app = Flask(__name__)

# Define a custom metric
request_count = Counter('flask_app_requests_total', 'Total number of requests')

@app.route('/')
def index():
    request_count.inc()  # Increment counter
    return "Hello, World! My name is Youssef Shawky and this is a simple python web app Automated by Jenkins and monitored by Prometheus"

@app.route('/metrics')
def metrics():
    return Response(generate_latest(), mimetype='text/plain')
