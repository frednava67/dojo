from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = 'antidisestablishmentarianism'

@app.route('/')
def index():
    if 'counter' in session:
        icounter = int(session['counter'])
        icounter+=1
        session['counter'] = icounter
    else:
        session['counter'] = 1
    return render_template('index.html', ctr=session['counter'])


@app.route('/destroy_session', methods=['POST'])
def destroyTheSession():
    cd = request.form['countdisplayed'] 
    print("Resetting counter from " + cd + "back to 1")
    session.clear()
    return redirect('/')

@app.route('/add2', methods=['POST'])
def Add2ToCounter():
    icounter = int(session['counter'])
    icounter+=1
    session['counter'] = icounter
    return redirect('/')    

if __name__ == "__main__":    # If __name__ is "__main__" we know we are running this file directly and not importing
                            # it from a different module
    app.run(debug=True)     # Run the app in debug mode.
