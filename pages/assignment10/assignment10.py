import mysql.connector
from interact_with_DB import interact_db
from flask import Blueprint, render_template, redirect, url_for, request, flash

# ‘assignment10’ blueprint definition
assignment10 = Blueprint('assignment10', __name__,
                         static_url_path='/pages/assignment10',
                         static_folder='static',
                         template_folder='templates')

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="root!"
)


# Routes
@assignment10.route('/assignment10', methods=['GET', 'POST'])
def assignment10_func():
    query='select * from users'
    users= interact_db(query=query, query_type='fetch')
    return render_template('assignment10.html', users= users)


