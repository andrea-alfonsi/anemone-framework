from attrs import frozen, field


@frozen
class DatasetMetadata:
    id: str = field(kw_only=True)
