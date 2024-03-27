from Veritabani import Database
from flask import *
from flask_login import LoginManager,UserMixin,login_user,logout_user,login_required
import EmailSender
from User import User

app=Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

@app.context_processor
def inject_variables():
    return dict(
        ViewBag=dict(error_message="",mails="",about="")
    )

@app.route("/")
def Index():
    about = Database.GetAbout()
    return render_template("Index.html", about=about)

@app.route("/Home")
def Home():
    about=Database.GetAbout()
    return render_template("Index.html",about=about)

@app.route("/About")
def About():
    about = Database.GetAbout()
    return render_template("About.html",about=about)

@app.route("/Contact")
def Contact():
    return render_template("Contact.html")

@app.route("/Login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        kullaniciAdi = request.form["username"]
        sifre = request.form["password"]
        result = Database.Login(kullaniciAdi, sifre)
        if result:  # Kullanıcı varsa result listesi boş olmayacaktır
            session['user'] = result
            if result[6]:
                session["admin"]=True
            error_message=True
            return redirect(url_for("Home"))
        else:
            return render_template("Login.html")
    else:
        return render_template("Login.html")

@app.route("/Logout")
def logout():
    session.pop('user')
    session.pop("admin")
    return redirect(url_for("Home"))

@app.route("/Register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        isim=request.form["name"]
        soyisim=request.form["surname"]
        eposta=request.form["email"]
        kullaniciAdi = request.form["username"]
        sifre = request.form["password"]
        tekrarsifre=request.form["repassword"]

        if tekrarsifre!=sifre:
            error_message="Şifreleriniz Uyuşmuyor"
            return render_template("Register.html",error_message=error_message)

        if isim =="" or soyisim=="" or kullaniciAdi=="" or eposta=="" or sifre =="" or tekrarsifre=="":
            error_message = "Alanlar Boş Geçilemez"
            return render_template("Register.html", error_message=error_message)

        if Database.UniqueUsername(kullaniciAdi):
            error_message = "Kullanıcı adı başka kullanıcı tarafından kullanılıyor."
            return render_template("Register.html", error_message=error_message)

        if Database.UniqueEmail(eposta):
            error_message = "Email başka kullanıcı tarafından kullanılıyor."
            return render_template("Register.html", error_message=error_message)

        user =User.Register(isim,soyisim,eposta,kullaniciAdi,sifre)

        result = Database.Register(user)
        if result==1:  # Kullanıcı varsa result listesi boş olmayacaktır
            return render_template("Login.html")
        else:
            return render_template("Register.html")
    else:
        return render_template("Register.html")

@app.route("/EmailGonder",methods=["POST"])
def EmailGonder():
    isim=request.form["name"]
    telefon=request.form["phone"]
    email=request.form["email"]
    mesaj=request.form["message"]

    EmailSender.Postala(isim,telefon,email,mesaj)
    Database.EmailSave(isim,telefon,email,mesaj)
    error_message="Email Gönderildi."
    return  render_template("Index.html",error_message=error_message)


@app.route("/Admin")
def Admin():
    if(session["user"][6]==True):
        return render_template("Admin.html")
    else:
        return  redirect(url_for("Home"))

@app.route("/Mail")
def Mail():
    mails = Database.GetMails()
    return render_template("Mail.html",mails=mails)

@app.route("/AdminAbout",methods=["GET","POST"])
def AdminAbout():
    if request.method=="GET":
        about = Database.GetAbout()
        return render_template("AdminAbout.html",about=about)
    else:
        about = Database.UpdateAbout(request.form["hakkimizda"])
        return render_template("AdminAbout.html", about=about)



if __name__=='__main__':
    app.run()