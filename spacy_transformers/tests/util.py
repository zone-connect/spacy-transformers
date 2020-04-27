from typing import Optional, Dict, List
import torch
import copy

from spacy.tokens import Doc
from thinc.api import Model

from ..types import TransformerOutput
from ..util import get_doc_spans
from ..wrapper import forward as transformer_forward


class DummyTokenizer:
    def __init__(self):
        self.str2int = {}
        self.int2str = {}
        self.start_symbol = "<s>"
        self.end_symbol = "</s>"

    def batch_encode_plus(
        self,
        texts: List[str],
        add_special_tokens: bool = True,
        max_length: Optional[int] = None,
        stride: int = 0,
        truncation_strategy: str = "longest_first",
        pad_to_max_length: bool = False,
        is_pretokenized: bool = False,
        return_tensors: Optional[str] = None,
        return_token_type_ids: Optional[bool] = None,
        return_attention_masks: Optional[bool] = None,
        return_overflowing_tokens: bool = False,
        return_special_tokens_masks: bool = False,
        return_offsets_mapping: bool = False,
        return_lengths: bool = False,
    ) -> Dict:
        output = {
            "input_ids": [],
            "attention_mask": [],
            "token_type_ids": [],
            "offset_mapping": [],
        }

        for text in texts:
            words, offsets, mask, type_ids = self._tokenize(text)
            ids = self._encode_words(words)
            output["input_ids"].append(ids)
            output["attention_mask"].append(mask)
            output["token_type_ids"].append(type_ids)
            output["offset_mapping"].append(offsets)
        output = self._pad(output)
        if return_tensors == "pt":
            output["input_ids"] = torch.tensor(output["input_ids"])
            output["attention_mask"] = torch.tensor(output["attention_mask"])
            output["token_type_ids"] = torch.tensor(output["token_type_ids"])
        return output

    def _pad(self, batch):
        batch = copy.deepcopy(batch)
        longest = max(len(ids) for ids in batch["input_ids"])
        for i in range(len(batch["input_ids"])):
            length = len(batch["input_ids"][i])
            difference = longest - length
            batch["attention_mask"][i] = [1] * length + [0] * difference
            batch["input_ids"][i].extend([0] * difference)
            batch["token_type_ids"][i].extend([2] * difference)
            batch["offset_mapping"][i].extend([None] * difference)
        return batch

    def _tokenize(self, text):
        offsets = []
        start = 0
        for i, char in enumerate(text):
            if char == " ":
                offsets.append((start, i))
                start = i + 1
        if start < len(text):
            offsets.append((start, len(text)))
        words = [text[start:end] for start, end in offsets]
        type_ids = [0] + [1] * len(words) + [0]
        words = [self.start_symbol] + words + [self.end_symbol]
        offsets = [None] + offsets + [None]
        mask = [1] * len(words)
        return words, offsets, mask, type_ids

    def _encode_words(self, words):
        ids = []
        for word in words:
            if word not in self.str2int:
                self.str2int[word] = len(self.str2int)
            ids.append(self.str2int[word])
        return ids


def DummyTransformerModel(width: int, depth: int):
    def _forward(model, tokens, is_train):
        width = model.attrs["width"]
        depth = model.attrs["depth"]
        tensors = []
        shape = (tokens.input_ids.shape[0], tokens.input_ids.shape[1], width)
        for i in range(depth):
            tensors.append(torch.zeros(*shape))
        return tensors, lambda d_tensors: tokens

    return Model("dummy-transformer", _forward, attrs={"width": width, "depth": depth})


def DummyTransformer(
    depth: int = 2, width: int = 4, get_spans=get_doc_spans
) -> Model[List[Doc], TransformerOutput]:
    """Create a test model that produces a TransformerOutput object."""
    return Model(
        "dummy-transformer",
        transformer_forward,
        layers=[DummyTransformerModel(width=width, depth=depth)],
        attrs={"get_spans": get_spans, "tokenizer": DummyTokenizer()},
        dims={"nO": width}
    )
