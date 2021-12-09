from flask import Flask, redirect, url_for

app = Flask(__name__)

@app.route('/home')
@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'

@app.route('/about')
def about_func():
    print('About page')
    return redirect('/desired')

@app.route('/catalog')
def catalog_func():
    return redirect(url_for('desired_func'))

@app.route('/desired')
def desired_func():
    return 'Welcome to the desired page!!!!'


if __name__ == '__main__':
    app.run(debug=True)
