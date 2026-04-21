# app.py

from flask import Flask, render_template
from config import Config
from database import init_db

# Import Blueprints
from auth import auth
from product import product
from dashboard import dashboard


# ==================================================
# CREATE APP
# ==================================================
app = Flask(__name__)
app.config.from_object(Config)


# ==================================================
# DATABASE INIT
# ==================================================
init_db(app)


# ==================================================
# SECRET KEY
# ==================================================
app.secret_key = Config.SECRET_KEY


# ==================================================
# REGISTER BLUEPRINTS
# ==================================================
app.register_blueprint(auth)
app.register_blueprint(product)
app.register_blueprint(dashboard)


# ==================================================
# PUBLIC ROUTES
# ==================================================
@app.route("/")
def home():
    return render_template("index.html")


# ==================================================
# ERROR HANDLERS
# ==================================================
@app.errorhandler(404)
def page_not_found(error):
    return render_template("404.html"), 404


@app.errorhandler(500)
def server_error(error):
    return render_template("500.html"), 500


# ==================================================
# RUN APP
# ==================================================
if __name__ == "__main__":
    app.run(debug=True)