from flask import Flask


def create_app():
  app = Flask(__name__)
  app.config['SECRET_KEY'] = "fsdafsdfdsfgfg fasdsadef"

  from .auth import auth
  from .views import views

  app.register_blueprint(views, url_pre_fix='/')
  app.register_blueprint(auth, url_pre_fix='/')


  return app