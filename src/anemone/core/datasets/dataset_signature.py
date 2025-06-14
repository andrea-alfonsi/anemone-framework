from attrs import frozen
from anemone.signatureflow import Signature


@frozen
class DatasetSignature:
    """
    Represents the signature of a dataset, defining its target and features.
    """

    targets: Signature
    features: Signature

    @property
    def signature(self) -> Signature:
        """
        Get all the columns signature ignoring the distincion features vs targets
        """
        s = {}
        for tk, tv in self.targets.items():
            s.setdefault(tk, tv)
        for fk, fv in self.features.items():
            s.setdefault(fk, fv)
        return s
