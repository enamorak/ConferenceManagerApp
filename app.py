from flask import Flask, render_template, request, redirect, url_for, jsonify
import mysql.connector

app = Flask(__name__)

# Подключение к базе данных
db = mysql.connector.connect(
    host="localhost",
    user="root",  # Ваш пользователь
    password="1234",  # Ваш пароль
    database="conference_manager"
)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/events')
def events():
    cursor = db.cursor(dictionary=True)
    cursor.execute("SELECT * FROM Events")
    events = cursor.fetchall()
    cursor.close()
    return render_template('events.html', events=events)

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']
        role = request.form['role']
        
        cursor = db.cursor()
        cursor.execute("INSERT INTO Users (name, email, password, role) VALUES (%s, %s, %s, %s)", (name, email, password, role))
        db.commit()
        cursor.close()
        
        return redirect(url_for('index'))
    return render_template('register.html')

@app.route('/surveys/<int:event_id>')
def surveys(event_id):
    cursor = db.cursor(dictionary=True)
    cursor.execute("SELECT * FROM Surveys WHERE event_id = %s", (event_id,))
    surveys = cursor.fetchall()
    cursor.close()
    return render_template('surveys.html', surveys=surveys)

@app.route('/api/events', methods=['GET'])
def api_events():
    cursor = db.cursor(dictionary=True)
    cursor.execute("SELECT * FROM Events")
    events = cursor.fetchall()
    cursor.close()
    return jsonify(events)

if __name__ == '__main__':
    app.run(debug=True)
