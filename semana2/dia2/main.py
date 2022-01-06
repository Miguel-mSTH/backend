import requests
from flask import Flask,render_template,request

URL='https://api.github.com/users/Miguel-mSTH'

data=requests.get(URL)
context =data.json()

app = Flask(__name__)

lstProductos = ['LAPTOP','IMPRESORA','PARLANTES']

@app.route('/index')
def index():
    #return 'HOLA MUNDO FLASK'
    nombre = request.args.get('nombre','no hay nombre')

    context = {
        'nombre':nombre,
        'productos':lstProductos
    }

    return render_template('index.html',**context)

@app.route('/')
def home():
    return render_template('home.html',**context)

@app.route('/portafolio')
def portafolio():
    return render_template('portafolio.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True,port=5000)