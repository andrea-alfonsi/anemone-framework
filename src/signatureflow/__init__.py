from typing import Callable, Union, get_args, get_origin, Type, Optional, Dict, Any, Sequence, Tuple
from collections.abc import Mapping
from collections import defaultdict
from inspect import Parameter, signature, Signature as inspectSignature
from .datatypes import DataType, Scalar, String

Signature = Mapping[str, DataType]


def infer_signature(func: Callable) -> Signature:
    def is_optional(parameter: Type) -> bool:
        is_union = get_origin(parameter) is Union
        can_be_none = type(None) in get_args(parameter)
        return is_union and can_be_none

    def infer_type(parameter_type: Type) -> Type[Union[String, Scalar]]:
        if parameter_type in (int, float, Optional[int], Optional[float]):
            return Scalar
        if parameter_type in (str, Optional[str]):
            return String
        raise ValueError(f"Cannot infer the type of parameter. Type `{ parameter_type.__name__}` is not supported.")

    def get_type_kwargs(param: Parameter) -> Dict[str, Any]:
        kwargs: Dict[str, Any] = {"required": not is_optional(param.annotation) and param.default is param.empty}
        if not param.default is param.empty:
            kwargs["default"] = param.default
        return kwargs

    if not callable(func):
        raise TypeError(f"Attempted to infer a signature for a non-callable. Got type '{type(func).__name__}'.")
    func_name = getattr(func, "__name__", repr(func))

    func_signature = signature(func)
    result: Dict[str, DataType] = {}

    for param in func_signature.parameters.values():

        if param.name == "self" or param.kind is param.VAR_KEYWORD or param.kind is param.VAR_POSITIONAL:
            continue  # self, *args, and **kwargs are not returned in inferred Specs.

        if param.annotation is param.empty and param.default is param.empty:
            raise TypeError(f"Unable to infer a type for parameter `{param.name}` of `{func_name}`.")

        param_type = type(param.default) if param.annotation is param.empty else param.annotation
        inferred_type = infer_type(param_type)

        result[param.name] = inferred_type(**get_type_kwargs(param))

    if func_signature.return_annotation is not inspectSignature.empty:
        # Return is a keyword so no parameter can be called "return"
        result["return"] = infer_type(func_signature.return_annotation)(
            required=not is_optional(func_signature.return_annotation)
        )

    return result


def validate_data(signature: Signature, data: Dict[str, Any]) -> Dict[str, Sequence[str]]:
    """
    Check if the data is comaptible with the given signature.
    Retuns a dictionary of errors that try to explain why the values are not valid.
    """
    errors: defaultdict[str, list[str]] = defaultdict(list)
    for key, dtype in signature.items():
        try:
            dtype.validate(data.get(key))
            dtype.validate_context(data)
        except ValueError as e:
            errors[key].append(str(e))
    return dict(errors)


def serialize(signature: Signature) -> Dict[str, Any]:
    """
    Convert a Signature into a dictionary
    """
    return {k: v.serialize() for k, v in signature.items()}


def transpose(source: Signature, target: Signature) -> Sequence[Tuple[str, str]]:
    mapping = []
    source_keys = source.keys()
    target_keys = target.keys()
    remaining = []

    for key in target_keys:
        if key in source_keys:
            if not type(source[key]) == type(target[key]):
                raise ValueError("The 2 signatures are not compatible")
            else:
                source_keys = [k for k in source_keys if not k == key]
        else:
            remaining.append(key)
    for key in remaining:
        for skey in source_keys:
            if type(source[skey]) == type(target[key]):
                mapping.append((skey, key))
                break
        else:
            raise ValueError(f"No key found comaptible with {key}")
    return mapping
