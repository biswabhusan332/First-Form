from flask import Flask, render_template, request
import csv
from pathlib import Path

app = Flask(__name__)

DATA_FILE = Path("form_data.csv")

@app.route("/", methods=["GET", "POST"])
def index():
    message = ""
    if request.method == "POST":
        name = request.form.get("name", "").strip()
        email = request.form.get("email", "").strip()
        comment = request.form.get("comment", "").strip()

        if name and email:
            new_file = not DATA_FILE.exists()
            with DATA_FILE.open("a", newline="") as f:
                writer = csv.writer(f)
                if new_file:
                    writer.writerow(["name", "email", "comment"])
                writer.writerow([name, email, comment])
            message = "Data saved successfully!"
        else:
            message = "Name and email are required."

    return render_template("form.html", message=message)
    
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
