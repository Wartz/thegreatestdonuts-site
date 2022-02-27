import os
from flask import Flask

def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY = "dev",
        DATABASE = os.path.join(app.instance_path, 'donutr.sqlite'),
    )
    if test_config is None:
            # load the instance config, if it exists, when not testing
            app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # a simple page that says hello
    @app.route('/')
    def index():
        return 'THE BEST DONUTS'
        
    # a simple page that shows a donut
    @app.route('/leaderboard')
    def leaderboard():
        return 'THE GREATEST DONUTS!'

    @app.route('/alldonuts/')
    def alldonuts():
        return 'All the donuts'

    return app
