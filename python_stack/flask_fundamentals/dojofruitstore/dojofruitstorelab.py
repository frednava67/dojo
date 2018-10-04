from flask import Flask, render_template, request, redirect
import datetime as dt
app = Flask(__name__)       

@app.route('/')
def showForm():
    return render_template('index.html')      

@app.route('/checkout', methods=["POST"])
def showResult():
    strawberries_ordered = request.form['strawberry_quantity']
    raspberries_ordered = request.form['raspberry_quantity']
    apples_ordered = request.form['apple_quantity'] 
    order_name = request.form['name']
    order_student_id = request.form['student_id']
    total_ordered = int(strawberries_ordered) + int(raspberries_ordered) + int(apples_ordered)   
    o_date = dt.datetime.now()
    order_date = o_date.strftime("%c")
    return render_template("ordersummary.html", order_date=order_date, total_ordered=int(total_ordered), strawberries_ordered=strawberries_ordered, raspberries_ordered=raspberries_ordered, apples_ordered=apples_ordered, order_name=order_name, order_student_id=order_student_id)    

if __name__=="__main__":
    app.run(debug=True)                   # Run the app in debug mode.