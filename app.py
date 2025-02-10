from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/borc-ekle")
def borc_ekle():
    return render_template("borc_ekle.html")

@app.route("/raporlar")
def raporlar():
    return render_template("raporlar.html")

@app.route("/ayarlar")
def ayarlar():
    return render_template("ayarlar.html")

if __name__ == "__main__":
    app.run(debug=True)
