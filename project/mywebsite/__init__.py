try:
    import os
    from flask import Flask
    from flask import (Flask, request,
                       render_template,
                       redirect, url_for,
                       session, send_file)
    from datetime import timedelta
except Exception as e:
    print("Some Modules are Missing {}".format(e))

app = Flask(__name__)
app.config["SECRET_KEY"] = "mysecretkey"
basedir = os.path.abspath(os.path.dirname(__file__))

from mywebsite.Home.views import home_blueprint
app.register_blueprint(home_blueprint, url_prefix="/home")