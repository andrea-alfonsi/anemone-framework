from logging import getLogger
from argparse import ArgumentParser
import importlib.util
import sys
import os
from flask import Flask, render_template_string

app = Flask(__name__)
parser = ArgumentParser()
logger = getLogger(__name__)
datasets = {}
models = {}


parser.add_argument("--host", default="0.0.0.0")
parser.add_argument("--port", default=8008)
parser.add_argument("--debug-server", action="store_true", default=False)
parser.add_argument("--layout", default=os.path.join(os.path.dirname(__file__), "layouts", "index.html"))
args = parser.parse_args()


@app.route("/", methods=["GET"])
def index():
    """
    Render the main application landing page
    """
    with open(args.layout, "r", encoding="utf-8") as f:
        html_content = f.read()
    return render_template_string(html_content, models=models, datasets=datasets)


def import_class(file_path: str, class_name: str):
    """
    Import classes dynamically at runtime
    """

    spec = importlib.util.spec_from_file_location("module.name", file_path)
    if spec is None:
        raise ValueError(f"Cannot load the file {file_path}")
    module = importlib.util.module_from_spec(spec)
    sys.modules["module.name"] = module
    if spec.loader is None:
        raise ValueError("An error occurred while loading the widget")
    spec.loader.exec_module(module)
    return getattr(module, class_name)


if __name__ == "__main__":
    app.run(
        host=args.host,
        port=args.port,
        debug=args.debug_server,
    )
