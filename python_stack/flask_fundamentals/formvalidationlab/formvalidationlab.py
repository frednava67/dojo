from flask import Flask, render_template, request, redirect, flash
app = Flask(__name__)       
app.secret_key = "ThisIsSecret!"

@app.route('/')
def showForm():
    return render_template('index.html')      

@app.route('/result', methods=["POST"])
def showResult():
    full_name = request.form['fullname']
    if len(request.form['fullname']) < 1:
        flash("Full Name cannot be blank!")
        return redirect('/')  
    loc = request.form['location']
    fav_lang = request.form['favorite_language'] 
    remarks = request.form['comment']
    if len(request.form['comment']) < 1:
        flash("Comment box cannot be blank!")
        return redirect('/')      
    elif len(request.form['comment']) > 120:
        flash("Comment box cannot be greater than 120 characters!")
        return redirect('/')          
    return render_template("display_info.html", full_name=full_name, loc=loc, fav_lang=fav_lang, remarks=remarks)    

if __name__=="__main__":
    app.run(debug=True)                   # Run the app in debug mode.