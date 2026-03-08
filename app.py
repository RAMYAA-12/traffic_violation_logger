from flask import Flask, render_template, request, redirect, url_for
from models import db, Violation
import qrcode, os

app = Flask(__name__)

# DB CONFIG
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///violations.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

# CREATE DB
with app.app_context():
    db.create_all()

# ---------------- ADD VIOLATION ----------------
@app.route("/", methods=["GET", "POST"])
def add_violation():

    if request.method == "POST":
        vehicle = request.form["vehicle"]
        vtype = request.form["type"]
        location = request.form["location"]
        date = request.form["date"]
        fine = request.form["fine"]

        record = Violation(vehicle_no=vehicle,
                           violation_type=vtype,
                           location=location,
                           date=date,
                           fine_amount=fine)

        db.session.add(record)
        db.session.commit()

        # QR CODE GENERATION
        qr_data = url_for("status", id=record.id, _external=True)

        if not os.path.exists("static/qr_codes"):
            os.makedirs("static/qr_codes")

        img = qrcode.make(qr_data)
        img.save(f"static/qr_codes/{record.id}.png")

        return redirect(url_for("view_history"))

    return render_template("add_violation.html")

# ---------------- VIEW HISTORY ----------------
@app.route("/history")
def view_history():
    vehicle = request.args.get("vehicle")

    if vehicle:
        records = Violation.query.filter_by(vehicle_no=vehicle).all()
    else:
        records = Violation.query.all()

    return render_template("view_history.html", records=records)

# ---------------- UPDATE STATUS ----------------
@app.route("/update/<int:id>")
def update_status(id):
    record = Violation.query.get_or_404(id)

    if record.status == "Unpaid":
        record.status = "Paid"
    else:
        record.status = "Unpaid"

    db.session.commit()
    return redirect(url_for("view_history"))

# ---------------- PUBLIC STATUS ----------------
@app.route("/status/<int:id>")
def status(id):
    record = Violation.query.get_or_404(id)
    return render_template("status.html", record=record)

# ---------------- RUN APP ----------------
if __name__ == "__main__":
    app.run(debug=True)
