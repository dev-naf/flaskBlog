# Melakukan Import Flask, render Template
from flask import Flask,render_template
# Melakukan import FLASK-WTF dan Validator
from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField
from wtforms.validators import DataRequired

# Create Instiate Flask App / Inisialisasi Flask
app =  Flask(__name__)
# Membuat Secret Key, Mencegah Pemalsuan Form
app.config['SECRET_KEY'] ='!!!'

# Class Form, digunakan untuk keperluan pembuatan FORM dan integrasi
# dengan Validator
class makeForm(FlaskForm):
    name = StringField("What's Your Name",validator=DataRequired)
    submit = SubmitField('Submit')

# membuat sebuah route
# Membuat routes dengan page
@app.route('/')
def index():
    name = "Ahnaf Fattah"
    stuff = "This is <strong> Bold Text </strong>"
    favCar = ["Toyota Kijang Innova", "Toyota Harier", "Mazda CX-5",3000]
    return render_template('index.html',name = name, stuff = stuff, favCar=favCar)

# Membuat route dengan Params
@app.route('/dev/<name>')
def devPage(name):
    return render_template('userProfile.html',data = name)

# Membuat Route page Name, untuk implementasi form
@app.route('/name',methods=['GET','POST'])
def namepage():
    return render_template('name.html')

# membuat Custom Error Page
# Invalid URL Error
@app.errorhandler(404)
def urlError(error):
    return render_template("404.html")

# membuat Custom Error Page
# Internal Server Error
@app.errorhandler(500)
def urlError(error):
    return render_template("500.html")

# Goal
# 1. init Flask [OK]
# 2. routing helloWorld [OK]
# 3. set Environtment developer, to start the dev.Server [OK]
# 4. And Route with Params [OK]
# 5. Add render Template With Create Folder Templates for access html Pages [OK]
# 6. Add Jinja [ok]
# 7. Pass Variable or Expression to HTML [ok]
# 8. Add Flilter in Expression [ok]
# 8a. Filter -> save, uppercase, lowercase, capitalize,title,trim, striptags [ok]
# 9. Add Jinja statements, looping or if statements [ok]
# 10. Add Custom Error Pages [OK]
# 11. Membuat SSH KEY public maupun private [OK]
# 12. Inisialisasi Public SSH KEY -> GitHUB [OK]
# 13. Membuat File .gitignore untuk mengabaikan file yang akan di commit [OK]
# 14. Membuat Repository dan melakukan PUSH [OK]
# 15. Membuat Template, dengan Jinja [OK] = Kita Tidak perlu membuat navbar disetiap page
# 16. Menggunakan Bootstrap pada Jinja [OK]
# 17. Membuat Navigation BAR [OK]
# 18. Modification NavBar [OK]
# 19. Menggunakan Expression Url_for pada href [OK]
# 20. Menggunakan Expression URL_FOR pada href, dengan parameter [OK]
# 21. Donwload Library flask-wtf [OK]
# 22. import flask-wtf dan wtforms,witform-validators [ok]
# 23. Membuat Secret Key [ok]
# 23. Membuat class form
# 24. Membuat Variable Textfield dan SubmitField + validator
# 25. Membuat Page 
# 26. Membuat Routing untuk page tersebut
# 27.

#https://www.youtube.com/watch?v=4yaG-jFfePc&list=PLCC34OHNcOtolz2Vd9ZSeSXWc8Bq23yEz&index=2