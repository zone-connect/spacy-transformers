# Stubs for torch.nn.modules.loss (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from ..._jit_internal import weak_module, weak_script_method
from .module import Module
from typing import Any, Optional

class _Loss(Module):
    reduction: Any = ...
    def __init__(self, size_average: Optional[Any] = ..., reduce: Optional[Any] = ..., reduction: str = ...) -> None: ...

class _WeightedLoss(_Loss):
    def __init__(self, weight: Optional[Any] = ..., size_average: Optional[Any] = ..., reduce: Optional[Any] = ..., reduction: str = ...) -> None: ...

class L1Loss(_Loss):
    __constants__: Any = ...
    def __init__(self, size_average: Optional[Any] = ..., reduce: Optional[Any] = ..., reduction: str = ...) -> None: ...
    def forward(self, input: Any, target: Any): ...

class NLLLoss(_WeightedLoss):
    __constants__: Any = ...
    ignore_index: Any = ...
    def __init__(self, weight: Optional[Any] = ..., size_average: Optional[Any] = ..., ignore_index: int = ..., reduce: Optional[Any] = ..., reduction: str = ...) -> None: ...
    def forward(self, input: Any, target: Any): ...

class NLLLoss2d(NLLLoss):
    def __init__(self, weight: Optional[Any] = ..., size_average: Optional[Any] = ..., ignore_index: int = ..., reduce: Optional[Any] = ..., reduction: str = ...) -> None: ...

class PoissonNLLLoss(_Loss):
    __constants__: Any = ...
    log_input: Any = ...
    full: Any = ...
    eps: Any = ...
    def __init__(self, log_input: bool = ..., full: bool = ..., size_average: Optional[Any] = ..., eps: float = ..., reduce: Optional[Any] = ..., reduction: str = ...) -> None: ...
    def forward(self, log_input: Any, target: Any): ...

class KLDivLoss(_Loss):
    __constants__: Any = ...
    def __init__(self, size_average: Optional[Any] = ..., reduce: Optional[Any] = ..., reduction: str = ...) -> None: ...
    def forward(self, input: Any, target: Any): ...

class MSELoss(_Loss):
    __constants__: Any = ...
    def __init__(self, size_average: Optional[Any] = ..., reduce: Optional[Any] = ..., reduction: str = ...) -> None: ...
    def forward(self, input: Any, target: Any): ...

class BCELoss(_WeightedLoss):
    __constants__: Any = ...
    def __init__(self, weight: Optional[Any] = ..., size_average: Optional[Any] = ..., reduce: Optional[Any] = ..., reduction: str = ...) -> None: ...
    def forward(self, input: Any, target: Any): ...

class BCEWithLogitsLoss(_Loss):
    __constants__: Any = ...
    def __init__(self, weight: Optional[Any] = ..., size_average: Optional[Any] = ..., reduce: Optional[Any] = ..., reduction: str = ..., pos_weight: Optional[Any] = ...) -> None: ...
    def forward(self, input: Any, target: Any): ...

class HingeEmbeddingLoss(_Loss):
    __constants__: Any = ...
    margin: Any = ...
    def __init__(self, margin: float = ..., size_average: Optional[Any] = ..., reduce: Optional[Any] = ..., reduction: str = ...) -> None: ...
    def forward(self, input: Any, target: Any): ...

class MultiLabelMarginLoss(_Loss):
    __constants__: Any = ...
    def __init__(self, size_average: Optional[Any] = ..., reduce: Optional[Any] = ..., reduction: str = ...) -> None: ...
    def forward(self, input: Any, target: Any): ...

class SmoothL1Loss(_Loss):
    __constants__: Any = ...
    def __init__(self, size_average: Optional[Any] = ..., reduce: Optional[Any] = ..., reduction: str = ...) -> None: ...
    def forward(self, input: Any, target: Any): ...

class SoftMarginLoss(_Loss):
    __constants__: Any = ...
    def __init__(self, size_average: Optional[Any] = ..., reduce: Optional[Any] = ..., reduction: str = ...) -> None: ...
    def forward(self, input: Any, target: Any): ...

class CrossEntropyLoss(_WeightedLoss):
    __constants__: Any = ...
    ignore_index: Any = ...
    def __init__(self, weight: Optional[Any] = ..., size_average: Optional[Any] = ..., ignore_index: int = ..., reduce: Optional[Any] = ..., reduction: str = ...) -> None: ...
    def forward(self, input: Any, target: Any): ...

class MultiLabelSoftMarginLoss(_WeightedLoss):
    __constants__: Any = ...
    def __init__(self, weight: Optional[Any] = ..., size_average: Optional[Any] = ..., reduce: Optional[Any] = ..., reduction: str = ...) -> None: ...
    def forward(self, input: Any, target: Any): ...

class CosineEmbeddingLoss(_Loss):
    __constants__: Any = ...
    margin: Any = ...
    def __init__(self, margin: float = ..., size_average: Optional[Any] = ..., reduce: Optional[Any] = ..., reduction: str = ...) -> None: ...
    def forward(self, input1: Any, input2: Any, target: Any): ...

class MarginRankingLoss(_Loss):
    __constants__: Any = ...
    margin: Any = ...
    def __init__(self, margin: float = ..., size_average: Optional[Any] = ..., reduce: Optional[Any] = ..., reduction: str = ...) -> None: ...
    def forward(self, input1: Any, input2: Any, target: Any): ...

class MultiMarginLoss(_WeightedLoss):
    __constants__: Any = ...
    p: Any = ...
    margin: Any = ...
    def __init__(self, p: int = ..., margin: float = ..., weight: Optional[Any] = ..., size_average: Optional[Any] = ..., reduce: Optional[Any] = ..., reduction: str = ...) -> None: ...
    def forward(self, input: Any, target: Any): ...

class TripletMarginLoss(_Loss):
    __constants__: Any = ...
    margin: Any = ...
    p: Any = ...
    eps: Any = ...
    swap: Any = ...
    def __init__(self, margin: float = ..., p: float = ..., eps: float = ..., swap: bool = ..., size_average: Optional[Any] = ..., reduce: Optional[Any] = ..., reduction: str = ...) -> None: ...
    def forward(self, anchor: Any, positive: Any, negative: Any): ...

class CTCLoss(_Loss):
    __constants__: Any = ...
    blank: Any = ...
    zero_infinity: Any = ...
    def __init__(self, blank: int = ..., reduction: str = ..., zero_infinity: bool = ...) -> None: ...
    def forward(self, log_probs: Any, targets: Any, input_lengths: Any, target_lengths: Any): ...