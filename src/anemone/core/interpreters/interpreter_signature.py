from attrs import frozen, field
from anemone.signatureflow import Signature


@frozen
class InterpreterSignature:
    config: Signature = field(kw_only=True)
    output: Signature = field(kw_only=True)
