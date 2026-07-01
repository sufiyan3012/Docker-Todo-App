from flask import Flask, render_template, request, redirect
import mysql.connector
from datetime import datetime
import time

app = Flask(__name__)

for i in range(30):
    try:
        db = mysql.connector.connect(
            host="mysql",
            user="root",
            password="root123",
            database="tododb"
        )
        print("Connected to MySQL")
        break
    except mysql.connector.Error as e:
        print(f"MySQL Error : {e}")
        print("Waiting for MySQL...")
        time.sleep(3)
else:
    raise Exception("Could not connect to MySQL")

cursor = db.cursor(dictionary=True)

@app.route("/", methods=["GET", "POST"])
def index():

    if request.method == "POST":
        task = request.form["task"]
        due_date = request.form["due_date"]

        created_date = datetime.now().strftime("%Y-%m-%d")

        sql = """
        INSERT INTO tasks
        (task, created_at, due_date)
        VALUES (%s, %s, %s)
        """

        values = (
            task,
            created_date,
            due_date if due_date else None
        )

        cursor.execute(sql, values)
        db.commit()

        return redirect("/")

    cursor.execute("SELECT * FROM tasks ORDER BY id DESC")
    tasks = cursor.fetchall()

    return render_template("index.html", tasks=tasks)


@app.route("/complete/<int:id>")
def complete(id):

    cursor.execute(
        "UPDATE tasks SET completed=1 WHERE id=%s",
        (id,)
    )

    db.commit()

    return redirect("/")


@app.route("/delete/<int:id>")
def delete(id):

    cursor.execute(
        "DELETE FROM tasks WHERE id=%s",
        (id,)
    )

    db.commit()

    return redirect("/")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
