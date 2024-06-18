import os
from flask import Flask

from rich.console import Console

console = Console()

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<h1>Flask Hello World!</h1>"


@app.route("/test/<username>")
def test(username):
    if username == "":
        return "Testing hidden functionality ;)\n"
    else:
        return f"Greetings {username}!"


if __name__ == "__main__":
    try:
        image_name = os.environ["PYTHON_IMAGE_NAME"]
    except:
        image_name = "unspecified"
    try:
        image_tag = os.environ["PYTHON_IMAGE_TAG"]
    except:
        image_tag = "unspecified"
    try:
        flask_ver = os.environ["FLASK_VER"]
    except:
        flask_ver = "unspecified"
    console.print(f"[green]Base Image is:[/] [cyan bold]{image_name}:{image_tag}[/]")
    console.print(f"[green]Flask version installed is:[/] {flask_ver}")
    app.run(host="0.0.0.0")
