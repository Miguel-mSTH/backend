from flask import Flask,jsonify,request
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow


app= Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='mysql://uuzhtpxkodkce4aw:9iYaOpAzBq4hU4fq1J53@bwdxuf9e5taunnynuurz-mysql.services.clever-cloud.com:3306/bwdxuf9e5taunnynuurz'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False

db=SQLAlchemy(app)
ma=Marshmallow(app)

#creamos tablas en la base de datos
class Alumno(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    nombre=db.Column(db.String(100),nullable=False)
    email=db.Column(db.String(100),unique=True)

    def __init__(self,nombre,email):
        self.nombre=nombre
        self.email=email

db.create_all()
print("Se crearon las tablas en la base de datos")

class AlumnosSchema(ma.Schema):
    class Meta:
        fields=('id','nombre','email')

alumno_schema = AlumnosSchema()

@app.route('/')
def index():
    return jsonify({'status':'OK','mensaje':'Bienvenido a mi APIREST con flask'})
#meotdo post para registrar alumnos
@app.route('/alumno',methods=['POST'])
def alumno():
    #capturamos los valores
    nombre=request.json['nombre']
    email=request.json['email']

    #insertamos el registro en la base de datos
    nuevoAlumno=Alumno(nombre,email)
    db.session.add(nuevoAlumno)
    db.session.commit()

    return alumno_schema.jsonify(nuevoAlumno)
#metodo get para consultar los alumnos
alumnos_schema=AlumnosSchema(many=True)

@app.route('/alumnos')
def alumnos():
    lstAlumnos=Alumno.query.all()
    dataAlumnos=alumnos_schema.dump(lstAlumnos)
    return jsonify(dataAlumnos)

#metodo put para actualizar alumnos
@app.route('/updalumno/<id>',methods=['PUT'])
def updateAlumno(id):
    alumno=Alumno.query.get(id)
    print(alumno)
    nombre=request.json['nombre']
    email=request.json['email']
    #actualizamos al alumno
    alumno.nombre=nombre
    alumno.email=email

    db.session.commit()

    return alumno_schema.jsonify(alumno)

#metodo delete para eliminar alumnos
@app.route('/delAlumno/<id>',methods=['DELETE'])
def deleteAlumno(id):
    alumno=Alumno.query.get(id)
    #eliminamos el alumno
    db.session.delete(alumno)
    db.session.commit()

    return alumno_schema.jsonify(alumno)

@app.route('/alumno/<id>')
def getAlumno(id):
    alumno=Alumno.query.get(id)
    return alumno_schema.jsonify(alumno)

if __name__ == "__main__":
    app.run(debug=True,port=5000)