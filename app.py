from flask import Flask, render_template, request
from flask_mysqldb import MySQL
app = Flask(__name__)


app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'pass'
app.config['MYSQL_DB'] = 'logtest'
print("111")
mysql = MySQL(app)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == "POST":
        details = request.form
        username = details['username1']
        password = details['password1']
        print("222")
        cur = mysql.connection.cursor()
        print("333")
        cur.execute("INSERT INTO accounts(username, password) VALUES (%s, %s)", (username, password))
        print("444")
        mysql.connection.commit()
        cur.close()
        return 'success'
    return render_template('index.html')


if __name__ == '__main__':
    app.run()
