from flask import Flask, render_template
app = Flask(__name__)       

@app.route('/')             
def buildDefaultBoard():
    return render_template('index.html', rows=8, columns=8)                            
                            
if __name__=="__main__":
    app.run(debug=True)                   # Run the app in debug mode.