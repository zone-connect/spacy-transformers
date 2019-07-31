# Stubs for torch._jit_internal (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any

compiled_weak_fns: Any
weak_script_methods: Any
weak_modules: Any
weak_types: Any
boolean_dispatched: Any
ignored_fns: Any
COMPILATION_PENDING: Any
COMPILED: Any

def createResolutionCallback(frames_up: int = ...): ...
def weak_script(fn: Any, _frames_up: int = ...): ...
def weak_module(cls): ...
def weak_script_method(fn: Any): ...
def boolean_dispatch(arg_name: Any, arg_index: Any, default: Any, if_true: Any, if_false: Any, module_name: Any, func_name: Any): ...
def ignore(fn: Any): ...
def is_tuple(ann: Any): ...
def is_list(ann: Any): ...
def is_dict(ann: Any): ...

class TupleCls:
    def __getitem__(self, types: Any): ...

class TupleInstance:
    __args__: Any = ...
    def __init__(self, types: Any) -> None: ...

class ListInstance:
    __args__: Any = ...
    def __init__(self, types: Any) -> None: ...

class ListCls:
    def __getitem__(self, types: Any): ...

class DictInstance:
    __args__: Any = ...
    def __init__(self, types: Any) -> None: ...

class DictCls:
    def __getitem__(self, types: Any): ...

class BroadcastingListCls:
    def __getitem__(self, types: Any) -> None: ...

BroadcastingList1: Any
