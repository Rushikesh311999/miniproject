


from flask import Flask, render_template, request
app = Flask(__name__)
@app.route('/Input', methods=['post', 'get'])
def login():
    message = ''
    if request.method == 'POST':
        Source = request.form.get('src')  # access the data inside 
        Destination = request.form.get('dest')
        Budget = request.form.get('bgt')
 
        message = "Enter details"
 
    return render_template('page1.html', message=message)

if __name__ == '__main__':
   app.run(debug = True)
