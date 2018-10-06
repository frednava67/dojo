from flask import Flask, render_template, request, redirect, session
import random as rnd

app = Flask(__name__)
app.secret_key = 'antidisestablishmentarianism'

@app.route('/')
def index():
    sn = 0
    guessesclasses = ""
    print("root route")
    if 'secretnumber' not in session:
        print("*"*25)
        print("secretnumber not in session")
        sn = rnd.randrange(0,101)
        print("secret number is ", sn)
        session['secretnumber'] = sn
        session['guessesclasses'] = " hidden "
        session['guess_result'] = ""
        print(session['guess_result'])
    print("*"*25)
    print("secretnumber in session")
    print(session['secretnumber'])
    print(session['guessesclasses'])
    print(session['guess_result'])
    return render_template('index.html', ctr=session['secretnumber'], divclasses=session['guessesclasses'], guessaccuracy=session['guess_result'])

@app.route('/destroy_session')
def destroyTheSession():
    print("Destroying Session")
    session.clear()
    return redirect('/')

@app.route('/check_guess', methods=['POST'])
def check_guess():
    sn = int(session['secretnumber'])
    session['guessesclasses']
    userguess = int(request.form['theguess'])
    print("the guess was " + str(userguess) + ", the secret number is " + str(sn))

    if sn > userguess:
        session['guess_result'] = "Too low!"
        print(session['guess_result'])
        session['guessesclasses'] = " redbox resultdiv center-block text-center "

    elif sn < userguess:
        session['guess_result'] = "Too high!"
        print(session['guess_result'])
        session['guessesclasses'] = " redbox resultdiv center-block text-center "   
    elif sn == userguess:
        session['guess_result'] = str(sn) + " was the number!"      
        session['guessesclasses'] = " greenbox resultdiv center-block text-center "

    return redirect('/') 

if __name__ == "__main__":    # If __name__ is "__main__" we know we are running this file directly and not importing
                            # it from a different module
    app.run(debug=True)     # Run the app in debug mode.
