from flask import Flask
from web_api.api import api

app = Flask(__name__)


# Put any additional blueprints here:
app.register_blueprint(api, url_prefix='/api')


@app.route("/")
def test():
    return "Server running"


if __name__ == '__main__':
    app.run(port=5000)
