from flask import Flask, render_template
from clinic_data import DOCTORS, SERVICES

app = Flask(__name__)


@app.get("/")
def home():
    return render_template(
        "index.html",
        doctors=DOCTORS,
        services=SERVICES,
    )

# if __name__ == "__main__":
#     app.run(debug=True)