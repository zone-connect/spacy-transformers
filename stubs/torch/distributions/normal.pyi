# Stubs for torch.distributions.normal (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from torch.distributions.exp_family import ExponentialFamily
from typing import Any, Optional

class Normal(ExponentialFamily):
    arg_constraints: Any = ...
    support: Any = ...
    has_rsample: bool = ...
    @property
    def mean(self): ...
    @property
    def stddev(self): ...
    @property
    def variance(self): ...
    def __init__(self, loc: Any, scale: Any, validate_args: Optional[Any] = ...) -> None: ...
    def expand(self, batch_shape: Any, _instance: Optional[Any] = ...): ...
    def sample(self, sample_shape: Any = ...): ...
    def rsample(self, sample_shape: Any = ...): ...
    def log_prob(self, value: Any): ...
    def cdf(self, value: Any): ...
    def icdf(self, value: Any): ...
    def entropy(self): ...
