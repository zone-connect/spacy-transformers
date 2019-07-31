# Stubs for torch.utils.data.dataset (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any

class Dataset:
    def __getitem__(self, index: Any) -> None: ...
    def __len__(self) -> None: ...
    def __add__(self, other: Any): ...

class TensorDataset(Dataset):
    tensors: Any = ...
    def __init__(self, *tensors: Any) -> None: ...
    def __getitem__(self, index: Any): ...
    def __len__(self): ...

class ConcatDataset(Dataset):
    @staticmethod
    def cumsum(sequence: Any): ...
    datasets: Any = ...
    cumulative_sizes: Any = ...
    def __init__(self, datasets: Any) -> None: ...
    def __len__(self): ...
    def __getitem__(self, idx: Any): ...
    @property
    def cummulative_sizes(self): ...

class Subset(Dataset):
    dataset: Any = ...
    indices: Any = ...
    def __init__(self, dataset: Any, indices: Any) -> None: ...
    def __getitem__(self, idx: Any): ...
    def __len__(self): ...

def random_split(dataset: Any, lengths: Any): ...
