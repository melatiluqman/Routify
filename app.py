from flask import Flask, render_template, request, redirect, url_for, session
from flask_mysqldb import MySQL
import MySQLdb.cursors
import re
from config import Config
# from utils.a_star import a_star_search
# from utils.csp import str_to_time, can_visit

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

@app.route('/planner', methods=['GET', 'POST'])
def planner():
    if request.method == 'POST':
        # Ambil data input pengguna
        departure_time = request.form.get('departure_time')
        return_time = request.form.get('return_time')
        start_point = request.form.get('start_point')
        end_point = request.form.get('end_point')
        transport_method = request.form['transport_method']
        destination1 = request.form.get('destination1')
        destination2 = request.form.get('destination2')
        destination3 = request.form.get('destination3')
        budget = request.form.get('budget')


        # Filter destinasi yang diisi (non-kosong)
        destinations = [d for d in [destination1, destination2, destination3] if d.strip()]  # Hilangkan spasi kosong

        # Periksa apakah minimal ada satu destinasi
        if not destinations:
            return render_template(
                'planner.html',
                error_message="Setidaknya satu destinasi harus diisi.",
                route=None,
                estimated_time=None
            )

        # Jalankan algoritma (contoh a_star)
        try:
            from utils.a_star import a_star_algorithm
            route, estimated_time = a_star_algorithm(
                start_point=start_point,
                destinations=destinations,
                end_point=end_point,
                departure_time=departure_time,
                return_time=return_time
            )
        except ImportError:
            route = []
            estimated_time = "Error: Algorithm not found."

        # Tampilkan hasil
        return render_template('planner.html', route=route, estimated_time=estimated_time)

    return render_template('planner.html', error_message=None, route=None, estimated_time=None)


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