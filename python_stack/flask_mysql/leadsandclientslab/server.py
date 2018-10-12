from flask import Flask, render_template, request, redirect, session
import datetime as dt

# import the function connectToMySQL from the file mysqlconnection.py
from mysqlconnection import connectToMySQL

app = Flask(__name__)
app.secret_key = 'antidisestablishmentarianism'

@app.route('/')
def index():

    if 'userprovideddaterange' not in session:
        mysql = connectToMySQL("lead_gen_business")
        sqlquery = "SELECT clients.first_name, clients.last_name, COUNT(*) as total_leads from leads JOIN sites ON leads.site_id = sites.site_id JOIN clients ON sites.client_id = clients.client_id GROUP BY clients.client_id ORDER BY total_leads DESC"
        print(sqlquery)
        leads_list = mysql.query_db(sqlquery)
    else:
        mysql = connectToMySQL("lead_gen_business")
        sqlquery = session['query']
        querydata = session['data']
        print(querydata, sqlquery)
        leads_list = mysql.query_db(sqlquery, querydata)

    return render_template('index.html', leadsList=leads_list)

@app.route('/update_list', methods=['POST'])
def update_list():
    fdate = request.form['from_date']
    tdate = request.form['to_date']

    print(fdate, tdate)

    if fdate == "" or tdate == "":
        return redirect('/')
    
    session.clear()

    query = "SELECT clients.first_name, clients.last_name, COUNT(*) as total_leads from leads JOIN sites ON leads.site_id = sites.site_id JOIN clients ON sites.client_id = clients.client_id WHERE leads.registered_datetime BETWEEN %(from_date)s AND %(to_date)s GROUP BY clients.client_id ORDER BY total_leads DESC"
    data =  {
                'from_date': fdate,
                'to_date':  tdate
            }
    
    session['query'] = query
    session['data'] = data
    session['userprovideddaterange'] = True

    return redirect('/')

if __name__ =="__main__":
    app.run(debug=True)