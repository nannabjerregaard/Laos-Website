<<<<<<< HEAD
from flask import Flask, render_template, request
import re

app = Flask(__name__)
EMAIL_REGEX = r'^[\w\.-]+@[\w\.-]+\.\w+$'

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        name = request.form.get("name").strip()
        email = request.form.get("email").strip()
        phone = request.form.get("phone").strip()
        message = request.form.get("message", "").strip()

        if not name:
            return "Name is required."
        if not email and not phone:
            return "Please provide at least an email or a phone number."
        if email and not re.match(EMAIL_REGEX, email):
            return "Invalid email address."

        return f"Thanks, {name}! We received your message."

    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
=======
from flask import Flask, render_template, request
import re

app = Flask(__name__)
EMAIL_REGEX = r'^[\w\.-]+@[\w\.-]+\.\w+$'

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        name = request.form.get("name").strip()
        email = request.form.get("email").strip()
        phone = request.form.get("phone").strip()
        message = request.form.get("message", "").strip()

        if not name:
            return "Name is required."
        if not email and not phone:
            return "Please provide at least an email or a phone number."
        if email and not re.match(EMAIL_REGEX, email):
            return "Invalid email address."

        return f"Thanks, {name}! We received your message."

    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
>>>>>>> c93aab5dfdeaf7a2a75d01258581d13a828b6ba6
