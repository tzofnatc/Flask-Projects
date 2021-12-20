from flask import Flask, redirect, url_for, render_template

app = Flask(__name__)

@app.route('/main')
@app.route('/')
def cv_func():
    return render_template('cv1.html')

@app.route('/ContactMe')
def contact_func():
    return render_template('ContactMe.html')


@app.route('/assignment8')
def assignment8_func():
    return render_template('assignment8.html',
                           valid=True,
                           Details={'name': 'Tzofnat','secondName':'Cohen'},
                           hobbies=('Dance', 'Music', 'Animals', 'Travel'),
                           Music='Rock')

if __name__ == '__main__':
    app.run(debug=True)
