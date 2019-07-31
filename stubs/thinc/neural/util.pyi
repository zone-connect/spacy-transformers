# Stubs for thinc.neural.util (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any, Optional

basestring = str
unicode = str

def get_array_module(x: Any): ...
def is_cupy_array(arr: Any): ...
def is_numpy_array(arr: Any): ...
def get_ops(ops: Any): ...
def prefer_gpu(): ...
def require_gpu(): ...
def minibatch(items: Any, size: int = ...) -> None: ...
def mark_sentence_boundaries(sequences: Any, drop: float = ...): ...
def remap_ids(ops: Any): ...
def copy_array(dst: Any, src: Any, casting: str = ..., where: Optional[Any] = ...) -> None: ...
def ensure_path(path: Any): ...
def to_categorical(y: Any, nb_classes: Optional[Any] = ...): ...
def flatten_sequences(sequences: Any, drop: float = ...): ...
def partition(examples: Any, split_size: Any): ...
