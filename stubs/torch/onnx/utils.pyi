# Stubs for torch.onnx.utils (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any, Optional

def is_in_onnx_export(): ...
def set_training(model: Any, mode: Any) -> None: ...
def export(model: Any, args: Any, f: Any, export_params: bool = ..., verbose: bool = ..., training: bool = ..., input_names: Optional[Any] = ..., output_names: Optional[Any] = ..., aten: bool = ..., export_raw_ir: bool = ..., operator_export_type: Optional[Any] = ..., opset_version: Optional[Any] = ..., _retain_param_name: bool = ..., do_constant_folding: bool = ..., strip_doc_string: bool = ...) -> None: ...
def export_to_pretty_string(model: Any, args: Any, f: Any, export_params: bool = ..., verbose: bool = ..., training: bool = ..., input_names: Optional[Any] = ..., output_names: Optional[Any] = ..., aten: bool = ..., export_raw_ir: bool = ..., operator_export_type: Optional[Any] = ..., export_type: Any = ..., example_outputs: Optional[Any] = ..., propagate: bool = ..., google_printer: bool = ..., opset_version: Optional[Any] = ..., _retain_param_name: bool = ...): ...

attr_pattern: Any
