from flask import Flask, render_template, request
import time

def create_app():
    app = Flask(__name__)

    @app.route('/')
    def index():
        return f'welcome'


    @app.route('/todo', methods=['GET', 'POST'])
    def todo():
        result = ""
        if request.method == 'POST':
            result = request.form['task']
        return render_template('todo.html', result=result)

    @app.route('/completed', methods=['GET'])
    def completed():
        priority = 1
        completed = 'no'
        thing = 'die'
        variables = [priority, thing, completed, time.strftime('%a %H:%M:%S')]
        return render_template('completed.html', thing=variables)


    return app