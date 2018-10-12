from flask import Flask, render_template, request, redirect, session
import random as rnd
import datetime as dt

app = Flask(__name__)
app.secret_key = 'pneumonoultramicroscopicsilicovolcanoconiosis'

#
# logDictionary format is: 
#
# logDictionary = [ logEntry = { "result": " winningAction ", "neutralAction" or " losingAction "
#                                "description": "[text goes here]"
#                              }
#                 ]
#

def goldGeneration(strChoice):
    if strChoice == "farm":
        gold = rnd.randint(10,20)
    elif strChoice == "cave":
        gold = rnd.randint(5,10)       
    elif strChoice == "house":
        gold = rnd.randint(2,5)  
    elif strChoice == "casino":
        gold = rnd.randint(-50,50)  
    return gold

@app.route('/')
def index():
    print("index()")
    show_restart_button = " btn btn-danger btn-block "

    if 'activity_log' not in session:
        show_restart_button = " btn btn-danger btn-block hidden "
        logDictionary = []
        session['activity_log'] = logDictionary
        session['current_gold'] = 0

    return render_template('index.html', winnings=int(session['current_gold']), summary=session['activity_log'], restart=show_restart_button)

@app.route('/destroy_session')
def destroyTheSession():
    print("destroyTheSession")
    session.clear()
    return redirect('/')

@app.route('/process_money', methods=['POST'])
def process_money():
    print("process_money()")

    logDictionary = session['activity_log']
    current_balance = session['current_gold']
    rightnow = dt.datetime.now()
    formattedDT = rightnow.strftime('%c')
    incoming_choice = request.form['action_choice']
    if incoming_choice == "kaboom":
        return redirect("/destroy_session")

    goldResult = goldGeneration(incoming_choice)
    current_balance += goldResult
    session['current_gold'] = current_balance

    if incoming_choice == "casino":
        if goldResult < 0:
            newlog = dict(result=" losingAction ", description="Entered a casino and lost " +  str(abs(goldResult)) + " gold... Ouch. (" + formattedDT + ")")
        elif goldResult > 0:
            newlog = dict(result=" winningAction ", description="Entered a casino and won " +  str(goldResult) + " gold... Excelsior! (" + formattedDT + ")")
        elif goldResult == 0:
            newlog = dict(result=" neutralAction ", description="Entered a casino and neither won or lost gold... Meh. (" + formattedDT + ")")
    else:
        newlog = dict(result=" winningAction ", description="Earned " +  str(goldResult) + " gold from the " + incoming_choice + "! (" + formattedDT + ")")

    logDictionary.insert(0, newlog)
    session['activity_log'] = logDictionary
    return redirect('/') 

if __name__ == "__main__":    # If __name__ is "__main__" we know we are running this file directly and not importing
                            # it from a different module
    app.run(debug=True)     # Run the app in debug mode.
