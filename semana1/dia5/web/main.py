from flask import Flask,render_template
from flask_mysqldb import MySQL
""" from flaskext.mysql import MySQL """


app = Flask(__name__)

#CONFIGURAR CONEXION CON BASE DE DATOS
app.config['MYSQL_HOST']='borfmkxnkhkdo8iwr7e3-mysql.services.clever-cloud.com'
app.config['MYSQL_USER']='ukal0etharhwcapg'
app.config['MYSQL_PASSWORD']='F4KJ7N3OgXfIT2EqdNv7'
app.config['MYSQL_DB']='borfmkxnkhkdo8iwr7e3'

mysql=MySQL(app)

@app.route('/')
def index():
    cursor=mysql.connection.cursor()
    cursor.execute('select id,sistema,procesador,memoria from computadoras')
    data=cursor.fetchall()
    cursor.close()
    print(data)

    context={
        'data':data
    }

    return render_template('index.html',**context)

app.run(debug=True,port=4000)