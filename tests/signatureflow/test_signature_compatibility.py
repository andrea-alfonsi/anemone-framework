from anemone.signatureflow import transpose
from anemone.signatureflow.datatypes.scalar import Scalar
from anemone.signatureflow.datatypes.string import String
import pytest


def test_empty_signatures():
    ssignature = dict()
    tsignature = dict()
    assert transpose(ssignature, tsignature) == []


def test_equal_signatures():
    ssignature = {"data": Scalar()}
    tsignature = ssignature
    assert transpose(ssignature, tsignature) == []


def test_source_greater_than_target():
    ssignature = {"data": Scalar(), "more": Scalar()}
    tsignature = {"data": Scalar()}
    assert transpose(ssignature, tsignature) == []


def test_simple_map():
    ssignature = {"data": Scalar()}
    tsignature = {"no_data": Scalar()}
    assert transpose(ssignature, tsignature) == [("data", "no_data")]


def test_not_compatible():
    ssignature = {"data": Scalar()}
    tsignature = {"data": String()}
    with pytest.raises(ValueError) as _:
        transpose(ssignature, tsignature)
