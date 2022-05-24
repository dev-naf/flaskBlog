# Melakukan Import Flask, render Template
from flask import Flask,render_template

# Create Instiate Flask App / Inisialisasi Flask

app =  Flask(__name__)

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
def name(name):
    return '<h1>Selamat Malam {}, Kamu sudah berhasil membuat app. Flask'.format(name)

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
# 11. Membuat SSH KEY public maupun private []
# 12. Inisialisasi Public SSH KEY -> GitHUB []
# 13. Membuat File .gitignore untuk mengabaikan file yang akan di commit
# 14. Membuat Repository dan melakukan PUSH []

#https://www.youtube.com/watch?v=4yaG-jFfePc&list=PLCC34OHNcOtolz2Vd9ZSeSXWc8Bq23yEz&index=2