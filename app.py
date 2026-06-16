from flask import Flask, render_template,request,redirect
import sqlite3

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def login():

    if request.method == 'POST':

        username = request.form['username']
        password = request.form['password']

        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()

        cursor.execute(
            "SELECT * FROM users WHERE username=? AND password=?",
            (username, password)
        )

        user = cursor.fetchone()

        conn.close()

        if user:
            return redirect('/dashboard')
        else:
            return "Invalid Username or Password"

    return render_template('login.html')
@app.route('/register', methods=['GET', 'POST'])
def register():

    if request.method == 'POST':

        username = request.form['username']
        email = request.form['email']
        password = request.form['password']

        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()

        cursor.execute(
            "INSERT INTO users(username,email,password) VALUES(?,?,?)",
            (username, email, password)
        )

        conn.commit()
        conn.close()

        return "Registration Successful!"

    return render_template('register.html')
@app.route('/sos', methods=['GET','POST'])
def sos():

    if request.method == 'POST':

        name = request.form['name']
        location = request.form['location']
        emergency_type = request.form['emergency_type']
        message = request.form['message']

        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()

        cursor.execute(
            "INSERT INTO alerts(name,location,emergency_type,message) VALUES(?,?,?,?)",
            (name, location, emergency_type, message)
        )

        conn.commit()
        conn.close()

        return "SOS Alert Sent Successfully!"

    return render_template('sos.html')
@app.route('/dashboard')
def dashboard():

    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM alerts")
    alerts = cursor.fetchall()

    cursor.execute("SELECT COUNT(*) FROM alerts")
    total_alerts = cursor.fetchone()[0]

    cursor.execute("SELECT COUNT(*) FROM alerts WHERE emergency_type='Flood'")
    flood_count = cursor.fetchone()[0]

    cursor.execute("SELECT COUNT(*) FROM alerts WHERE emergency_type='Fire'")
    fire_count = cursor.fetchone()[0]

    cursor.execute("SELECT COUNT(*) FROM alerts WHERE emergency_type='Earthquake'")
    earthquake_count = cursor.fetchone()[0]

    cursor.execute("SELECT COUNT(*) FROM alerts WHERE emergency_type='Medical Emergency'")
    medical_count = cursor.fetchone()[0]

    conn.close()

    routes = []

    for alert in alerts:

        if alert[2] == "Coimbatore":
            route = "📡 Node A → Node C → Rescue Center"

        elif alert[2] == "Pollachi":
            route = "📡 Node B → Node D → Rescue Center"

        else:
            route = "📡 Node A → Node B → Rescue Center"

        routes.append(route)

    return render_template(
        'dashboard.html',
        alerts=alerts,
        routes=routes,
        total_alerts=total_alerts,
        flood_count=flood_count,
        fire_count=fire_count,
        earthquake_count=earthquake_count,
        medical_count=medical_count
    )
if __name__ == '__main__':
    app.run(debug=True)