# Stubs for thinc.neural._classes.selu (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from ...describe import Biases, Dimension, Gradient, Synapses
from .model import Model
from typing import Any, Optional

class SELU(Model):
    name: str = ...
    @property
    def input_shape(self): ...
    @property
    def output_shape(self): ...
    nO: Any = ...
    nI: Any = ...
    drop_factor: Any = ...
    def __init__(self, nO: Optional[Any] = ..., nI: Optional[Any] = ..., **kwargs: Any) -> None: ...
    def predict(self, input__bi: Any): ...
    def begin_update(self, input__bi: Any, drop: float = ...): ...
    def dropout(self, X: Any, finish_update: Any, drop: Any): ...
