from flask inport flask

app = Flask(__name__)


@app.route("/")
def index():
    return "THIS IS WORKING"


if __name__ = "__main__":
    app.run()
