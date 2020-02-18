from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')  # se crea una ruta para pagina principal
def home():
    return render_template('home.html')  # se mostrara en el navegador inicialmente

@app.route('/about')  # se crea una ruta para pagina about
def about():
    return render_template('about.html') 

if __name__ == '__main__': # la pagina se queda escuchando
     app.run(debug=True)              #inicia la pagina       

      #"static/css/main.css"

      #"{{ url_for('static', filename='css/main.css') }}"> 