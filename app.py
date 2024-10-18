from flask import Flask

#This creates an instance of the Flask class, representing your web application.
app = Flask(__name__)

#This is a route decorator that defines the URL path. In this case, it’s the homepage (/).
@app.route('/')

# This function is executed when the homepage is accessed and returns a simple message.
def home():
    return "Hello, World! My name is Youssef Shawky and this is a simple python web app Automated by jenkins."


if __name__ == '__main__':  #a common Python idiom used to control the behavior of a script when it's run directly.
    app.run(host='0.0.0.0' , port=5000)  #This starts the web server and makes the app accessible, host='0.0.0.0' ensures it can be accessed externally, and port=5000 sets the port.
