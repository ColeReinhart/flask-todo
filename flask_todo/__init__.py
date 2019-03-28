from flask import Flask, render_template, request
import time, psycopg2

localtime = time.asctime( time.localtime(time.time()) )

def create_app():
    app = Flask(__name__)
    # connection to database
    con = psycopg2.connect(
                host = "localhost",
                database="flask_todo"
    )
    #cursor
    cur = con.cursor()

    # execute query
    

    @app.route('/', methods=['GET', 'POST'])
    def todo():
        if request.method == 'POST':
            result = request.form['task']
            cur.execute("INSERT INTO todos (task, completed, created) VALUES (%s,%s,%s)",(result, False, localtime))
            con.commit()
  
        return render_template('todo.html')
    @app.route('/tasks', methods=['GET','POST'])
    def task():
        cur.execute("select task,created from todos")
        rows = cur.fetchall()
       
        return render_template('tasks.html', thing=rows)
    @app.route('/completed', methods=['GET'])
    def completed():
        cur.execute("select task,created from todos WHERE completed = 'yes'")
        rows = cur.fetchall()

        return render_template('completed.html', thing=rows)

  
    return app
    con.close()
    cur.close()