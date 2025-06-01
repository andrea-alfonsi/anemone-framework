from attrs import frozen, field


@frozen
class DatasetMetadata:
    name: str = field(kw_only=True)
