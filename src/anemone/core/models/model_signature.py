from attrs import frozen, field
from anemone.signatureflow import Signature


@frozen
class ModelSignature:
    input: Signature = field(kw_only=True)
    output: Signature = field(kw_only=True)
