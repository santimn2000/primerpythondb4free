from flask import Flask, render_template, flash, request, Response, jsonify, redirect, url_for
from database import app, db, EstudianteSchema
from estudiante import Estudiante

student_schema = EstudianteSchema()
students_schema = EstudianteSchema(many=True)

@app.route('/')
def home():
    estudiantes = Estudiante.query.all()
    estudiantesLeidos = students_schema.dump(estudiantes)
    return render_template('index.html', estudiantes = estudiantesLeidos)

    # return jsonify(estudiantesLeidos)

#Method Post
@app.route('/estudiantes', methods=['POST'])
def addEstudiante():
    nombre = request.form['nombre']
    apellidos = request.form['apellidos']
    email = request.form['email']
    edad = request.form['edad']
    bio = request.form['bio']

    if nombre and apellidos and email and edad and bio:
        nuevo_estudiante = Estudiante(nombre, apellidos, email, edad, bio)
        db.session.add(nuevo_estudiante)
        db.session.commit()
        response = jsonify({
            'nombre' : nombre,
            'apellidos' : apellidos,
            'email' : email, 
            'edad' : edad,
            'bio' : bio
        })
        return redirect(url_for('home'))
    else:
        return notFound()

#Method delete
@app.route('/delete/<id>')
def deleteEstudiante(id):
    estudiante = Estudiante.query.get(id)
    db.session.delete(estudiante)
    db.session.commit()
    
    flash('Estudiante ' + id + ' eliminado correctamente')
    return redirect(url_for('home'))

#Method Put
@app.route('/edit/<id>', methods=['POST'])
def editEstudiante(id):    
    
    nombre = request.form['nombre']
    apellidos = request.form['apellidos']
    email = request.form['email']
    edad = request.form['edad']
    bio = request.form['bio']
    
    if nombre and apellidos and email and edad and bio:
        estudiante = Estudiante.query.get(id)
  # return student_schema.jsonify(student)
        estudiante.nombre = nombre
        estudiante.apellidos = apellidos
        estudiante.email = email
        estudiante.edad = edad
        estudiante.biografia = bio
        
        db.session.commit()
        
        response = jsonify({'message' : 'Estudiante ' + id + ' actualizado correctamente'})
        flash('Estudiante ' + id + ' modificado correctamente')
        return redirect(url_for('home'))
    else:
        return notFound()

@app.errorhandler(404)
def notFound(error=None):
    message ={
        'message': 'No encontrado ' + request.url,
        'status': '404 Not Found'
    }
    response = jsonify(message)
    response.status_code = 404
    return response

if __name__ == '__main__':
    app.run(debug=True, port=5000)