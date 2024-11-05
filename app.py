from flask import Flask
from prometheus_client import Counter, Histogram, generate_latest

#This creates an instance of the Flask class, representing your web application.
app = Flask(__name__)

REQUEST_COUNT = Counter('app_request_count', 'Total request count')
REQUEST_LATENCY = Histogram('app_request_latency_seconds', 'Request latency')

#This is a route decorator that defines the URL path. In this case, it’s the homepage (/).
@app.route('/')

# This function is executed when the homepage is accessed and returns a simple message.
def home():
    REQUEST_COUNT.inc()
    with REQUEST_LATENCY.time():
        return "Hello, World! My name is Youssef Shawky and this is a simple python web app Automated by Jenkins."

@app.route('/metrics')
def metrics():
    return generate_latest()

if __name__ == '__main__':  #a common Python idiom used to control the behavior of a script when it's run directly.
    app.run(host='0.0.0.0' , port=5000)  #This starts the web server and makes the app accessible, host='0.0.0.0' ensures it can be accessed externally, and port=5000 sets the port.

