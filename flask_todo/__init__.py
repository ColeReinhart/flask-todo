from flask import Flask, render_template, request
import time, psycopg2

# connection to database
con = psycopg2.connect(
            host = "localhost",
            database="flask_todo"
)
#cursor
cur = con.cursor()

# execute query
cur.execute("select * from todos")

rows = cur.fetchall()

for r in rows:
    print(r)
#commiting changes


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
        cur.execute("INSERT INTO todos (task, completed, created) VALUES ('{result}', 'no', 'today')")
        con.commit()

        return render_template('todo.html', result=rows)

    @app.route('/completed', methods=['GET'])
    def completed():
        # todos = {'thing': 'clean garage', 'completed': 'False'}
        # variables = [todos['thing'], todos['completed']]
        return render_template('completed.html', thing=rows)

    
    return app
    #close the cursor
    cur.close()
    # close the connection
    con.close()