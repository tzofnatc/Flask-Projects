import mysql.connector
from interact_with_DB import interact_db
from flask import Blueprint, render_template, redirect, url_for, request, flash

## ‘assignment10’ blueprint
assignment10 = Blueprint('assignment10', __name__,
                         static_url_path='/pages/assignment10',
                         static_folder='static',
                         template_folder='templates')

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="root"
)

# Routes
@assignment10.route('/assignment10', methods=['GET', 'POST'])
def assignment10_func():
    query='select * from users'
    users= interact_db(query=query, query_type='fetch')
    return render_template('assignment10.html', users= users)

@assignment10.route('/insert_user', methods=['post'])
def insert_users_func():
    # get the data
    name = request.form['name']
    email = request.form['email']
    gender = request.form['gender']

    #insert to DB
    query = "insert into users(name, email, gender) values ('%s','%s','%s'); " % (name, email, gender)
    interact_db(query=query, query_type='commit')

    # come back to users
    flash('New user has been insert!')
    return redirect('/assignment10')


@assignment10.route('/update_user', methods=['post'])
def update_users_func():
    # get the data
    id = request.form['id']
    name = request.form['name']
    email = request.form['email']
    gender = request.form['gender']

    #update DB

    query = "select id FROM users WHERE id = '%s';" % id
    query_result = interact_db(query=query, query_type='fetch')
    if len(query_result) > 0:
        query = "UPDATE users SET name = '%s', email = '%s' ,gender = '%s' where id='%s' ; " % (name, email, gender ,id)
        interact_db(query=query, query_type='commit')
        flash('User has been updated!')
        return redirect('/assignment10')
    else:
        flash(f'id user {id} not exist')
        return redirect('/assignment10')

@assignment10.route('/delete_user', methods=['post'])
def delete_user_func():
    user_id= request.form['id']
    query= "delete from users where id='%s';" % user_id
    interact_db(query=query, query_type='commit')
    flash('User has been Deleted!')
    return redirect("/assignment10")
