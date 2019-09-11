from flask import Flask,render_template
import matplotlib
import numpy

app = Flask(__name__)

@app.route('/a')
def index():
 
   
   return render_template('hello.html',res="a")

if __name__ == '__main__':
   app.run(debug = True)
