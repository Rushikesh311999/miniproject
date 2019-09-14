from flask import Flask, redirect, url_for, request, render_template, abort, jsonify
app = Flask(__name__)
# serving form request from website
@app.route('/send_data/', methods=['POST'])
def send_data():
    if request.method == 'POST':
        #set up connection and send data to server
        msg="successful"
        return redirect(url_for('main_page', message=msg))

@app.route('/main_page/<message>/')
def main_page(message):
    return render_template('page2.html')

@app.route('/start_trip/')
def start_trip():
       return render_template('page1.html')

if __name__ == '__main__':
   app.run(debug = True)
