from flask import Flask, render_template     # Import Flask to allow us to create our app.
app = Flask(__name__)       # Global variable __name__ tells Flask whether or not we are running the file
                            # directly, or importing it as a module.
print(__name__)             # Just for fun, print __name__ to see what it is

@app.route('/show')
def show_user():
  return render_template('user.html', name='Jay', email='kpatel@codingdojo.com')

if __name__=="__main__":    # If __name__ is "__main__" we know we are running this file directly and not importing
                            # it from a different module
    app.run(debug=True)     # Run the app in debug mode.

