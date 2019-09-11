from flask import Flask,render_template
import matplotlib
import numpy

app = Flask(__name__)

@app.route('/a')
def index():
   #a=request.firm[""source"]
                  #connection setup with server
                  #[],{}
   
   return render_template('hello.html',res="a")

if __name__ == '__main__':
   app.run(debug = True)
