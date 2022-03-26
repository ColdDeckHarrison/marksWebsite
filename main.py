from flask import Flask, render_template, request
import smtplib


app = Flask(__name__)

MY_EMAIL = "pythonautomail87@gmail.com"
MY_PASSWORD = "otsasee1234"


@app.route('/')
def run_app():
    return render_template("index.html")

@app.route('/countries')
def countries():
    return render_template("countries.html")


@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        data = request.form
        name = data["name"]
        email = data["email"]
        phone = data["phone"]
        message = data["message"]
        with smtplib.SMTP("smtp.gmail.com", 587) as connection:
            connection.starttls()
            connection.login(MY_EMAIL, MY_PASSWORD)
            connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs=MY_EMAIL,
                msg=f"Contact Me \n{name}\n{email}\n{phone}\n{message}")
    return render_template("contact.html")


if __name__ == "__main__":
    app.run(debug=True)
