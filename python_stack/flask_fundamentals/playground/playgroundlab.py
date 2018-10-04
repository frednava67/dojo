from flask import Flask, render_template     # Import Flask to allow us to create our app.
app = Flask(__name__)       # Global variable __name__ tells Flask whether or not we are running the file
                            # directly, or importing it as a module.
print(__name__)             # Just for fun, print __name__ to see what it is

@app.route('/')             # The "@" symbol designates a "decorator" which attaches the following
                            # function to the '/' route. This means that whenever we send a request to
                            # localhost:5000/ we will run the following "hello_world" function.
def hello_world():
    return 'Hello World!'   # Return the string 'Hello World!' as a response.

@app.route('/play')
def play():
    return render_template('index.html', times=3, bgcolor="lightblue")

@app.route('/play/<iterations>')
def play2(iterations):
    return render_template('index.html', times=int(iterations), bgcolor="lightblue")

@app.route('/play/<iterations>/<color>')
def play3(iterations, color):
    return render_template('index.html', times=int(iterations), bgcolor=color)

if __name__=="__main__":
    app.run(debug=True)                   # Run the app in debug mode.