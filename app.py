from flask import Flask, render_template
from flask_mysqldb import MySQL

app = Flask(__name__)
import re

app = Flask(__name__)
mysql = MySQL(app)

# Configure DB
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = '123456'
app.config['MYSQL_DB'] = 'logtest'

print("connect successful!!")


@app.route('/')
def users():
    cur = mysql.connection.cursor()
    cur.execute('''SELECT id, username, password FROM accounts''')
    aa = cur.fetchall()
    return render_template('index.html', aa=aa)


if __name__ == '__main__':
    app.run(debug=True)
