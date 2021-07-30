from flask import Flask, render_template, redirect, request

app = Flask(__name__)

# Rotas

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/courses')
def courses():
    return render_template('courses.html')

@app.route('/about')
def about():
    return render_template('about.html')

# Executa o server

if __name__ == '__main__':
    app.run(debug=True)