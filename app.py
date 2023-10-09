from flask import Flask, url_for, render_template, redirect, request, url_for
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'crud'

mysql = MySQL(app)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/insert', methods = ['GET', 'POST'])
def insert():
    if request.method == "POST":
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']

        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO crud(name, email, phone) VALUES(%s, %s, %s)", (name, email, phone))
        mysql.connection.commit()
        return redirect(url_for('index'))

if __name__ == "__main__":
    app.run(debug=True)