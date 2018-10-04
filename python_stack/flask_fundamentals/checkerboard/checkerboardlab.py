from flask import Flask, render_template
app = Flask(__name__)       

@app.route('/')
def buildDefaultBoard():
    return render_template('index.html', rows=8, columns=8)                            

@app.route('/<rows>/<columns>')
def buildCustomSizeBoard(rows, columns):
    return render_template('index.html', rows=int(rows), columns=int(columns))                            

@app.route('/<rows>/<columns>/<color1>/<color2>')
def buildCustomSizeAndColorBoard(rows, columns, color1, color2):
    return render_template('index.html', rows=int(rows), columns=int(columns), c1=color1, c2=color2)

if __name__=="__main__":
    app.run(debug=True)                   # Run the app in debug mode.