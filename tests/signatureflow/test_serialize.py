from anemone.signatureflow import validate_data, serialize
from anemone.signatureflow.datatypes import Scalar, String, Tensor


def test_scalar():
    signature = {"temperature": Scalar()}
    assert serialize(signature) == {
        "temperature": {
            "align": None,
            "default": 0.0,
            "required": True,
            "type": "Scalar",
            "min": None,
            "max": None,
            "step": None,
        }
    }


def test_string():
    signature = {"message": String()}
    assert serialize(signature) == {"message": {"align": None, "default": "", "required": True, "type": "String"}}


def test_composition():
    signature = {"temperature": Scalar(), "message": String()}
    assert serialize(signature) == {
        "temperature": {
            "align": None,
            "default": 0.0,
            "required": True,
            "type": "Scalar",
            "min": None,
            "max": None,
            "step": None,
        },
        "message": {"align": None, "default": "", "required": True, "type": "String"},
    }
