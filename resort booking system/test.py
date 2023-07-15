from flask import Flask,render_template,url_for,request
# import pymysql
# def connector():
#     conn=pymysql.connect(
#         user='root',password='850885@nithish',db='resortbooking',host='localhost')
#     cursor=conn.cursor()
#     return conn,cursor
app=Flask(__name__)
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
@app.route('/',methods=['GET','POST'])
def home():
    
    return render_template("index.html")
if __name__=="__main__":
    app.debug=True
    app.run()

