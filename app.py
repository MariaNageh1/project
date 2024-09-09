from flask import Flask, render_template, redirect, url_for, request, session # type: ignore
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user # type: ignore
from models import User, Doctor, db # type: ignore

app = Flask(__name__)
app.secret_key = 'your_secret_key'
login_manager = LoginManager()
login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(username=username, password=password).first()
        if user:
            login_user(user)
            return redirect(url_for('home'))
    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        new_user = User(username=username, password=password)
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('login'))
    return render_template('registration.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))

@app.route('/')
@login_required
def home():
    specializations = ['Dentist', 'Cardiologist', 'Neurologist']  # Example data
    areas = ['City Center', 'Downtown', 'City Nasser']  # Example data
    return render_template('home.html', specializations=specializations, areas=areas)

@app.route('/search', methods=['POST'])
@login_required
def search():
    specialization = request.form['specialization']
    area = request.form['area']
    doctors = Doctor.query.filter_by(specialization=specialization, area=area).all()
    return render_template('home.html', doctors=doctors)

@app.route('/doctor/<int:doctor_id>')
@login_required
def doctor_details(doctor_id):
    doctor = Doctor.query.get_or_404(doctor_id)
    return render_template('doctor_details.html', doctor=doctor)

if __name__ == '__main__':
    app.run(debug=True)
