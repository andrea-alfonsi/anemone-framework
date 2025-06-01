from anemone.signatureflow import infer_signature
from anemone.signatureflow.datatypes import Scalar, String
from typing import Optional
import pytest


def test_empty_function():
    def empty_function():
        pass

    signature = infer_signature(empty_function)
    assert signature == dict()


def test_fibonacci():
    def fib(n: int):
        if n == 1 or n == 2:
            return 1
        return fib(n - 1) + fib(n - 2)

    signature_fib = infer_signature(fib)
    assert signature_fib.get("n") == Scalar(required=True)


def test_hello_name():
    def hello(name="world"):
        print("Hello", name)

    hello_signature = infer_signature(hello)
    assert hello_signature.get("name") == String(required=False, default="world")


def test_multi_args_function():
    def repeat(name: str, times: int = 1):
        [print(name) for _ in range(times)]

    repeat_signature = infer_signature(repeat)
    assert repeat_signature.get("name") == String(required=True)
    assert repeat_signature.get("times") == Scalar(required=False, default=1)


def test_with_return():
    def hi() -> str:
        return "Hello world"

    def optional_hi() -> Optional[str]:
        return None

    hi_signature = infer_signature(hi)
    optional_signature = infer_signature(optional_hi)
    assert hi_signature.get("return") == String(required=True)
    assert optional_signature.get("return") == String(required=False)


def test_function_with_datatypes():
    def func(s: Scalar):
        pass

    with pytest.raises(ValueError):
        infer_signature(func)
