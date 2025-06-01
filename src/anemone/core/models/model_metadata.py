"""
This module defines the `ModelMetadata` class, which encapsulates metadata related to
machine learning models, including their name and trainability status
"""

from attrs import frozen, field


@frozen
class ModelMetadata:
    """
    Stores metadata information for a machine learning model.
    """

    name: str = field(kw_only=True)
    trainable: bool = field(kw_only=True)
