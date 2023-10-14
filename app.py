from flask import Flask, url_for, render_template, redirect, request, url_for, flash
from flask_mysqldb import MySQL

app = Flask(__name__)

app.secret_key = 'flash message'

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'crud'

mysql = MySQL(app)

@app.route('/')
def index():
    row = {'key': 'value'}

    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM list")
    data = cur.fetchall()
    cur.close()

    return render_template('index.html', list = data, row=row)


@app.route('/insert', methods = ['GET', 'POST'])
def insert():
    if request.method == "POST":
        flash("Data Inserted Successfully")
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']

        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO list(name, email, phone) VALUES(%s, %s, %s)", (name, email, phone))
        mysql.connection.commit()
        return redirect(url_for('index'))
    


@app.route('/update',methods=['POST','GET'])
def update():

    if request.method == 'POST':
        id_data = request.form['id']
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
        cur = mysql.connection.cursor()
        cur.execute("""
               UPDATE list
               SET name=%s, email=%s, phone=%s
               WHERE id=%s
            """, (name, email, phone, id_data))
        flash("Data Updated Successfully")
        mysql.connection.commit()
        return redirect(url_for('index'))


@app.route('/delete/<string:id_data>', methods = ['GET', 'POST'])
def delete(id_data):
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM list WHERE id = %s", (id_data))
    mysql.connection.commit()
    return redirect(url_for('index'))



if __name__ == "__main__":
    app.run(debug=True)