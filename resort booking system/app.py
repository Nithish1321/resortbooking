from flask import Flask,render_template,url_for,request, redirect

import pymysql
def sql_connector():
    conn=pymysql.connect(
        user='root',password='850885@nithish',db='resortbooking',host='localhost')
    cursor=conn.cursor()
    return conn,cursor
app=Flask(__name__)
@app.route('/home/')
def hom():
    return render_template("index.html")
@app.route('/explore/')
def exp():
    return render_template("explore.html")
@app.route('/rooms/')
def room():
    return render_template("rooms.html")
@app.route('/bb/')
def bb():
    return render_template("bb.html")
@app.route('/contact/')
def contact():
    return render_template("contact.html")



@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        name = request.form.get('username')
        email = request.form.get('email')
        password = request.form.get('password')
        conn, c = sql_connector()
        c.execute("INSERT INTO signup VALUES ('{}','{}','{}')".format(
            name, email, password))
        conn.commit()
        conn.close()
        c.close()
        print(name, email, password)

    return render_template("index1.html")
@app.route('/bb/', methods=['GET', 'POST'])
def hello():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        room = request.form.get('Rooms')
        No_of_roooms = request.form.get('number1')
        No_of_guest = request.form.get('number2')
        Timing = request.form.get('date1')
        conn, c = sql_connector()
        c.execute("INSERT INTO booking VALUES ('{}','{}','{}','{}','{}','{}')".format(
            name, email, room, No_of_roooms, No_of_guest,Timing))
        conn.commit()
        conn.close()
        c.close()
        print(name, email,room, No_of_roooms, No_of_guest,Timing)

    return render_template("bb.html")


@app.route('/contact/', methods=['GET', 'POST'])
def tess():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        message = request.form.get('message')
      
        conn, c = sql_connector()
        c.execute("INSERT INTO contact VALUES ('{}','{}','{}')".format(
            name, email, message,))
        conn.commit()
        conn.close()
        c.close()
        print(name, email, message)

    return render_template("contact.html")


@app.route('/app.py', methods=['POST'])
def login():
   
    username = request.form['Username1']
    password = request.form['password1']

   
    connection = pymysql.connect(host='localhost',
                                 user='root',
                                 password='850885@nithish',
                                 database='resortbooking')
    cursor = connection.cursor()

    # Execute a SELECT query to check if the provided username and password match a record in the database
    query = "SELECT * FROM signup WHERE username = %s AND password = %s"
    cursor.execute(query, (username, password))

    result = cursor.fetchone()

    # Close the cursor and the database connection
    cursor.close()
    connection.close()

    if result:
        # Redirect to a success page if login is successful
        return render_template("index.html")
        
    else:
        # Redirect back to the login page with an error message if login fails
        return redirect(url_for("nit", name="Invalid Login!"))


@app.route("/<name>")
def nit(name):
    return render_template("index1.html",content=name)


if __name__=="__main__":
    app.debug=True
    app.run()