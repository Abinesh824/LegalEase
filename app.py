from flask import Flask, render_template, request

app = Flask(__name__)

TEMPLATES = {
    "nda": """
NON-DISCLOSURE AGREEMENT

This Agreement is made between {party1} and {party2}.

Purpose:
{purpose}

Both parties agree to keep confidential information private.

Date: {date}
""",

    "employment": """
EMPLOYMENT AGREEMENT

Employer: {party1}
Employee: {party2}

Job Role:
{purpose}

Start Date: {date}
"""
}


@app.route("/", methods=["GET", "POST"])
def index():
    generated = ""

    if request.method == "POST":
        doc_type = request.form["doc_type"]

        generated = TEMPLATES[doc_type].format(
            party1=request.form["party1"],
            party2=request.form["party2"],
            purpose=request.form["purpose"],
            date=request.form["date"]
        )

    return render_template("index.html", generated=generated)


if __name__ == "__main__":
    app.run(debug=True)
