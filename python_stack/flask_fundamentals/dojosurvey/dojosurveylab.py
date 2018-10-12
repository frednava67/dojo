from flask import Flask, render_template, request, redirect
app = Flask(__name__)       

@app.route('/')
def showForm():
    return render_template('index.html')      

@app.route('/result', methods=["POST"])
def showResult():
    full_name = request.form['fullname']
    loc = request.form['location']
    fav_lang = request.form['favorite_language'] 
    remarks = request.form['comment']
    return render_template("display_info.html", full_name=full_name, loc=loc, fav_lang=fav_lang, remarks=remarks)    

if __name__=="__main__":
    app.run(debug=True)                   # Run the app in debug mode.