from typing import Dict, Literal, Sequence, Union
from json import loads

def validate_select( query: Dict[str, Union[str, Sequence[str]]] ):
  """
  Check is a string is a valid select query
  Only json objects are valid for now
  """
  if not isinstance( query, dict ):
    raise ValueError("The select must be a dict")
  if not ( query.get("select") is None or (isinstance( query.get( "select" ), list ) and all([isinstance(x, str) for x in query.get("select", [0])])) ):
    raise ValueError("`select` must be missing or a list of strings")
  if not ( query.get("conditions") is None or (isinstance( query.get( "conditions" ), list ) and all([isinstance(x, str) for x in query.get("conditions", [0])])) ):
    raise ValueError("`conditions` must be missing or a list of strings")
  if not ( query.get("order") is None or (isinstance( query.get( "order" ), list ) and all([isinstance(x, str) for x in query.get("order", [0])])) ):
    raise ValueError("`order` must be missing or a list of strings")



def validate_select_str( query: str ):
  return validate_select( loads(query) )