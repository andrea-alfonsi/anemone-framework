import argparse
from flask import Flask, g, render_template
from typing import Optional
import logging
from core.models.base import BaseModel, ModelSignature

from core.datasets.dataset_signature import DatasetSignature
from pandas import DataFrame
from signatureflow import Scalar, String, serialize

app = Flask(__name__)
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


def parse_args():
    parser = argparse.ArgumentParser(description="Gunicorn App with Argument Parsing")
    parser.add_argument("--model", action="append", help="List of models", required=False)
    parser.add_argument("--dataset", action="append", help="List of datasets", required=False)
    parser.add_argument("--port", help="Listen on port", default=5000, required=False)

    return parser.parse_args()


args = parse_args()
example_model1 = BaseModel(
    "My Model 1",
    ModelSignature(
        input={"temperature": Scalar(), "message": String(default="Hi, what's your name? ")}, output={"y": Scalar()}
    ),
)
example_model2 = BaseModel(
    "My Model 2", ModelSignature(input={"age": Scalar(), "score": Scalar()}, output={"y": Scalar()})
)

MODELS = {"0": example_model1, "1": example_model2}
DATASETS = {}


@app.route("/")
def home():
    return render_template("home.html", models=MODELS, datasets=DATASETS)


@app.route("/info/<component>/<id>")
def info(component: str, id: Optional[str] = None):
    if component not in ("app", "model", "dataset", "interpreter"):
        return ("The component must be any of `app`, `model`,`dataset` or `interpreter`"), 400
    if not component == "app" and id is None:
        return ("The requested component requires an id"), 400
    if component == "model":
        model = bool(id) and MODELS.get(id)
        if model:
            return serialize(model.signature.input)
        return {"error": "Cannot find the requested model"}
    if component == "dataset":
        pass
    return {"models": args.model, "datasets": args.dataset, "id": id}


@app.route("/run/<id>")
def run_interpreter(id: str):
    return {"result": "ok"}


if __name__ == "__main__":
    app.run(debug=True)
