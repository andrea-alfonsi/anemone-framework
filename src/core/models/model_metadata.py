from attrs import frozen, field


@frozen
class ModelMetadata:
    id: str = field(kw_only=True)
    trainable: bool = field(kw_only=True)
