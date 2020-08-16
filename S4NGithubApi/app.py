from flask import Flask

from S4NGithubApi.rest import GitHubAPIREST
from S4NGithubApi.settings import DevConfig


def create_app(config_object=DevConfig):
    app = Flask(__name__)
    app.config.from_object(config_object)
    app.register_blueprint(GitHubAPIREST.blueprint)
    return app