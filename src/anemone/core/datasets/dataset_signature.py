from attrs import frozen, field
from anemone.signatureflow import Signature


@frozen
class DatasetSignature:
    signature: Signature = field(kw_only=True)
