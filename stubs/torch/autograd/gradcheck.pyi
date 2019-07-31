# Stubs for torch.autograd.gradcheck (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any, Optional

def zero_gradients(x: Any) -> None: ...
def make_jacobian(input: Any, num_out: Any): ...
def iter_tensors(x: Any, only_requiring_grad: bool = ...) -> None: ...
def get_numerical_jacobian(fn: Any, input: Any, target: Optional[Any] = ..., eps: float = ...): ...
def get_analytical_jacobian(input: Any, output: Any): ...
def gradcheck(func: Any, inputs: Any, eps: float = ..., atol: float = ..., rtol: float = ..., raise_exception: bool = ..., check_sparse_nnz: bool = ...): ...
def gradgradcheck(func: Any, inputs: Any, grad_outputs: Optional[Any] = ..., eps: float = ..., atol: float = ..., rtol: float = ..., gen_non_contig_grad_outputs: bool = ..., raise_exception: bool = ...): ...
