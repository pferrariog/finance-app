from finance.extensions.config import init_app
from flask import Flask


def create_app():
    """Create a configured Flask instance"""

    app = Flask(__name__)

    init_app(app)

    return app


if __name__ == "__main__":
    app = create_app()
    app.run()
