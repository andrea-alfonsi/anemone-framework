from signatureflow import validate_data
from signatureflow.datatypes import Scalar, String
from typing import Optional


def test_simple_json():
    signature = {"name": String(required=True), "age": Scalar(required=False)}

    assert len(validate_data(signature, {"name": "John"}).keys()) == 0
    assert len(validate_data(signature, {"name": "John", "age": 3}).keys()) == 0
    assert len(validate_data(signature, {"age": 3}).get("name", [])) == 1
    assert len(validate_data(signature, {"name": "John", "age": "3"}).get("age", [])) == 1
