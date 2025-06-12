from flask import Flask, render_template, request, redirect, url_for, session
import mysql.connector

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# Configure MySQL connection
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Digidara1000",
    database="devi"
)

@app.route('/')
@app.route('/home1')
def home1():
    return render_template('home1.html')

@app.route('/teams')
def teams():
    return render_template('teams.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/admin')  # login page
def admin_login():
    return render_template('login.html')

@app.route("/login", methods=["GET", "POST"])
def login():
    error = None
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        if username == 'admin123' and password == '1234':
            session['admin'] = True
            return redirect(url_for("admin_dashboard"))  # fixed redirect
        else:
            error = "Invalid username or password"
    return render_template("login.html", error=error)

@app.route("/admin/dashboard")
def admin_dashboard():
    if not session.get('admin'):
        return redirect(url_for("admin_login"))  # fixed redirect to login
    return render_template("admin.html")

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        data = (
            request.form.get('name'),
            request.form.get('dob'),
            request.form.get('gender'),
            request.form.get('email'),
            request.form.get('phone'),
            request.form.get('address'),
            request.form.get('emergency_contact'),
            request.form.get('emergency_phone'),
            request.form.get('sport'),  
            request.form.get('sport_level'),
            request.form.get('skill_level'),
            request.form.get('experience'),
            request.form.get('medical_info'),
            request.form.get('allergies'),
            request.form.get('conditions'),
            request.form.get('medications')
        )
        try:
            with db.cursor() as cursor:
                cursor.execute("""
                    INSERT INTO registrations 
                    (name, dob, gender, email, phone, address, emergency_contact, emergency_phone, sport, sport_level, skill_level, experience, medical_info, allergies, conditions, medications)
                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                """, data)
                db.commit()
        except Exception as e:
            return f"<h2>Error: {e}</h2>"
        return redirect(url_for('success'))
    return render_template('register.html')

@app.route('/success')
def success():
    return "<h2>Registration successful!</h2>"

if __name__ == '__main__':
    app.run(debug=True)
