# Stubs for thinc.v2v (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from .neural._classes.affine import Affine
from .neural._classes.maxout import Maxout
from .neural._classes.model import Model
from .neural._classes.relu import ReLu
from .neural._classes.selu import SELU

class Softmax(Affine):
    name: str = ...
    def predict(self, input__BI: Any): ...
    def begin_update(self, input__BI: Any, drop: float = ...): ...
