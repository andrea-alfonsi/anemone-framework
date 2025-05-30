from attrs import frozen, field
from signatureflow import Signature


@frozen
class DatasetSignature:
    signature: Signature = field(kw_only=True)
