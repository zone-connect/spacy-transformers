# Stubs for torch.nn.parallel.distributed_cpu (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from torch.nn.modules import Module
from typing import Any

class DistributedDataParallelCPU(Module):
    module: Any = ...
    needs_reduction: bool = ...
    def __init__(self, module: Any) -> None: ...
    def sync_parameters(self) -> None: ...
    def forward(self, *inputs: Any, **kwargs: Any): ...
