from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return "<h1><strong>Esta es la página de About.</strong></h1><p>Esta es una página de ejemplo para mostrar cómo funciona Flask.</p>"
#renderizar paginas para reutilizar codigo
#flask permite mandar es decir soporta listas y diccionarios
#{{ t }} permite iterar (esta en tasks) la t puede ser otra variable mas comoda pero tambien afectaria al for 
#creado en tasks
#guardando los cambios



@app.route('/tasks')
def list_tasks():
    tarea = ["Lavar la ropa","Limpiar la casa","Hacer la compra", "Estudiar para el examen","Hacer ejercicio","Leer un libro"]
    return render_template('tasks.html', t=tarea)

if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=5001)