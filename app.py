from flask import Flask, redirect, url_for, render_template, request, session, jsonify
from pages.assignment10.interact_with_DB import interact_db
import requests


app = Flask(__name__)
app.secret_key= '123'

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


@app.route('/assignment9', methods=['GET', 'POST'])
def assignment9_func():
    users = {'user1': {'name': 'Yael', 'gender': 'Female', 'email': 'yael@gmail.com'},
             'user2': {'name': 'Niv', 'gender': 'Male', 'email': 'niv23@gmail.com'},
             'user3': {'name': 'Tzofnat', 'gender': 'Female', 'email': 'tzofi@gmail.com'},
             'user4': {'name': 'Sapir', 'gender': 'Female', 'email': 'sap123@gmail.com'},
             'user5': {'name': 'Ori', 'gender': 'Female', 'email': 'ori456@gmail.com'}
             }

    if request.method == 'GET':
        if 'user_id' in request.args:
            if request.args.get('user_id') != '':
                user_id = request.args['user_id']
                for id in users:
                    if id == user_id:
                        user_name = users[id]['name']
                        email = users[id]['email']
                        gender = users[id]['gender']
                        return render_template('assignment9.html', user_name=user_name, email=email, gender=gender)
                return render_template('assignment9.html',not_found='not')
            return render_template('assignment9.html',  users=users)
        return render_template('assignment9.html')

    if request.method == 'POST':
        user_nickname= request.form['nickname']
        password= request.form['password']
        found= True
        if found:
            session['user_nickname'] = user_nickname
            session['user_password'] = password
            return render_template('assignment9.html')
        else:
            return render_template('assignment9.html')


@app.route('/logout')
def logout_func():
    session['user_nickname'] = ''
    session['user_password'] = ''
    return render_template('assignment9.html')

if __name__ == '__main__':
    app.run(debug=True)


## assignment10
from pages.assignment10.assignment10 import assignment10
app.register_blueprint(assignment10)

## assignment11
@app.route('/assignment11/users')
def assignment11_users():
    query = "select * from users"
    query_result = interact_db(query=query, query_type='fetch')
    response = jsonify(query_result)
    return response

@app.route('/assignment11/outer_source', methods=['GET', 'POST'])
def assignment11_outer_source():
    return render_template('assignment11.html')

@app.route('/front_outer_source', methods=['post'])
def req_frontend_func():
     user_id = request.form['user_id']
     return render_template('assignment11.html', id=user_id)

@app.route('/backend_outer_source')
def req_backend_func():
    if request.args['user_id'] != '':
        id = request.args['user_id']
        res = requests.get(f'https://reqres.in/api/users/{id}')
        user = res.json()
    return render_template('assignment11.html', user=user)

@app.route('/assignment12/restapi_users', defaults ={'user_id': 1})
@app.route('/assignment12/restapi_users/<int:user_id>')
def get_user_func(user_id):
    query = "select * from users where id='%s';"%(user_id)
    users = interact_db(query=query, query_type='fetch')
    if len(users)==0:
        return_db={
            'Status': 'Failed',
            'Message': 'User not found in DB!'
        }
    else:
         return_db={
            'Status' : 'Success',
            'id':users[0].id,
            'name': users[0].name,
            'email': users[0].email,
        }
    return jsonify(return_db)