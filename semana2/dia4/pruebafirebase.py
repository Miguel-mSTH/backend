import pyrebase

config = {
    "apiKey": "AIzaSyCKj489F-DiRAF9LxVX1DqW2tuvPtdS_jM",
    "authDomain": "portafolio-375f8.firebaseapp.com",
    "databaseURL": "https://portafolio-375f8-default-rtdb.firebaseio.com",
    "projectId": "portafolio-375f8",
    "storageBucket": "portafolio-375f8.appspot.com",
    "messagingSenderId": "1060382071238",
    "appId": "1:1060382071238:web:832847a62faf3252aafac7",
    "measurementId": "G-YR1Y6NKMJY"
}

firebase = pyrebase.initialize_app(config)

#ejemplos con auth
auth = firebase.auth()
usuario=auth.sign_in_with_email_and_password('pmespinoza@lamolina.edu.pe','codigo2022')
print(auth.get_account_info(usuario['idToken']))

auth.delete_user_account(usuario['idToken'])

print("enviando email de verificacion")
auth.send_email_verification(usuario['idToken'])

#cambiando la contrasena del usuario
auth.send_password_reset_email('pablo.tecusp@tecsup.edu.pe')
print("se envio un correo de reseteo de password")

#crear usuarios
email=input("Ingresa email : ")
password = input("Ingrese password : ")

auth.create_user_with_email_and_password(email,password)
print("Usuario creado con exito ")