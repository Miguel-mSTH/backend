from flask import Flask,render_template
from whitenoise import WhiteNoise

import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

cred = credentials.Certificate("firebasetoken.json")
firebase_admin.initialize_app(cred)
db=firestore.client()


app=Flask(__name__)
app.wsgi_app=WhiteNoise(app.wsgi_app,root='static/')

@app.route('/')
def home():
    context={
        'nombre':'miguel espinoza',
        'imagen':'',
        'bio':'Full Stack Developer 2'
    }
    return render_template('home.html',**context)

@app.route('/portafolio')
def portafolio():
    colProyectos=db.collection('proyectos')
    docProyectos=colProyectos.get()

    lstProyectos=[]
    for doc in docProyectos:
        print(doc.to_dict())
        dicProyecto=doc.to_dict()
        lstProyectos.append(dicProyecto)

    context={
        'proyectos':lstProyectos
    }

    return render_template('portafolio.html',**context)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True,port=5000)