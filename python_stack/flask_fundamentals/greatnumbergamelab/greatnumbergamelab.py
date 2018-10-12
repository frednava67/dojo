from flask import Flask, render_template, request, redirect, session
import random as rnd

app = Flask(__name__)
app.secret_key = 'antidisestablishmentarianism'

@app.route('/')
def index():
    print("index()")
    sn = 0
    if 'secretnumber' not in session:
        sn = rnd.randrange(0,101)
        print("secret number is ", sn)
        session['secretnumber'] = sn
        session['guessesclasses'] = " hidden "
        session['btnclasses'] = " hidden "
        session['guess_result'] = ""
        session['userguessdiv'] = " "
    return render_template('index.html', ugdiv=session['userguessdiv'], playagainbtn=session['btnclasses'], ctr=session['secretnumber'], divclasses=session['guessesclasses'], guessaccuracy=session['guess_result'])

@app.route('/destroy_session')
def destroyTheSession():
    print("destroyTheSession")
    session.clear()
    return redirect('/')

@app.route('/reset_game', methods=['POST'])
def resetTheGame():
    print("resetTheGame()")    
    session.clear()
    return redirect('/')

@app.route('/check_guess', methods=['POST'])
def check_guess():
    print("check_guess()")
    sn = int(session['secretnumber'])
    tg = request.form['theguess']

    if tg == "":
        tg = "0"
    userguess = int(tg)

    if sn > userguess:
        session['guess_result'] = "Too low!"
        session['guessesclasses'] = " redbox resultdiv center-block text-center "
    elif sn < userguess:
        session['guess_result'] = "Too high!"
        session['guessesclasses'] = " redbox resultdiv center-block text-center "   
    elif sn == userguess:
        session['guess_result'] = str(sn) + " was the number!"      
        session['guessesclasses'] = " greenbox resultdiv center-block text-center "
        session['btnclasses'] = " btn btn-info "
        session['userguessdiv'] = " hidden "
    return redirect('/') 

if __name__ == "__main__":    # If __name__ is "__main__" we know we are running this file directly and not importing
                            # it from a different module
    app.run(debug=True)     # Run the app in debug mode.
