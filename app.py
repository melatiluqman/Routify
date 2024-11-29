from flask import Flask, render_template, request, redirect, url_for, session
from flask_mysqldb import MySQL
import MySQLdb.cursors
import re
from config import Config

# Initialize Flask app
app = Flask(__name__)
app.config.from_object(Config)

# Initialize MySQL
mysql = MySQL(app)


@app.route('/')
@app.route('/login', methods=['GET', 'POST'])
def login():
    message = ''
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        if not email or not password:
            message = 'Email and Password are required!'
        else:
            cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
            cursor.execute(
                'SELECT * FROM user WHERE email = %s AND password = %s', (email, password))
            user = cursor.fetchone()

        if user:
            session['loggedin'] = True
            session['userid'] = user['userid']
            session['name'] = user['name']
            session['email'] = user['email']
            return redirect(url_for('home'))  # Ubah dari render_template ke redirect
        else:
            message = 'Invalid email or password!'

    return render_template('login.html', message=message)


@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('login'))


@app.route('/register', methods=['GET', 'POST'])
def register():
    message = ''
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        password = request.form.get('password')
        phone = request.form.get('phone')
        country = request.form.get('country')
        city = request.form.get('city')

        # countries_cities = {
        #             'Indonesia': ["Jakarta", "Surabaya", "Bandung", "Medan", "Denpasar"]
        #         }

        # Validate input
        if not name or not email or not password or not country or not city or not phone:
            message = 'All fields are required!'
        elif not re.match(r'[^@]+@[^@]+\.[^@]+', email):
            message = 'Invalid email format!'
        elif not re.match(r'^\+?[0-9]{10,15}$', phone):  # Validasi nomor telepon
            message = 'Invalid phone number!'
        # elif city not in countries_cities[country]:
        #     message = f'City "{city}" is not valid for country "{country}"!'
        else:
            cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
            cursor.execute('SELECT * FROM user WHERE email = %s', (email,))
            account = cursor.fetchone()

            if account:
                message = 'Account already exists!'
            else:
                # Masukkan data ke tabel
                cursor.execute(
                    'INSERT INTO user (name, email, password, country, city, phone) VALUES (%s, %s, %s, %s, %s, %s)',
                    (name, email, password, country, city, phone)
                )
                mysql.connection.commit()
                message = 'Registration successful!'

    return render_template('register.html', message=message)

@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/planner')
def planner():
    return render_template('planner.html')

@app.route('/profile')
def profile():
    return render_template('profile.html')

@app.route('/settings')
def settings():
    return render_template('settings.html')

@app.route('/history')
def history():
    return render_template('history.html')



if __name__ == '__main__':
    app.run(debug=True)
