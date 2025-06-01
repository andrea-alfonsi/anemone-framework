from attrs import frozen, field


@frozen
class ModelMetadata:
    name: str = field(kw_only=True)
    trainable: bool = field(kw_only=True)
