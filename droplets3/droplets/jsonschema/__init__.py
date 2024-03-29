"""
An implementation of JSON Schema for Python

The main functionality is provided by the validator classes for each of the
supported JSON Schema versions.

Most commonly, :func:`validate` is the quickest way to simply validate a given
instance under a schema, and will create a validator for you.

"""

from .exceptions import (
    FormatError, RefResolutionError, SchemaError, ValidationError
)
from ._format import (
    FormatChecker, draft3_format_checker, draft4_format_checker,
)
from .validators import (
    ErrorTree, Draft3Validator, Draft4Validator, RefResolver, validate
)


__version__ = "2.1.0-dev"


# flake8: noqa
