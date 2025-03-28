from flask import Flask

from .commandos import register_commands
from .controllers import NewUserController, UserListController
from .config import Config, DevelopmentConfig

def create_app(config:Config= None):
    app = Flask('mvc')
    if config is None:
        app.config.from_object(DevelopmentConfig)
    else:
        app.config.from_object(config)

    register_commands(app)  
    app.add_url_rule("/", view_func = UserListController.as_view("get_lijst"))
    app.add_url_rule("/nieuw", view_func=NewUserController.as_view("nieuwe_klant"))

    return app