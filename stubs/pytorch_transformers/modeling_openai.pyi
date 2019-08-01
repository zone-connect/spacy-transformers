# Stubs for pytorch_transformers.modeling_openai (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

import torch.nn as nn
from .modeling_utils import CONFIG_NAME, Conv1D, PreTrainedModel, PretrainedConfig, SequenceSummary, WEIGHTS_NAME, add_start_docstrings, prune_conv1d_layer
from typing import Any, Optional

logger: Any
OPENAI_GPT_PRETRAINED_MODEL_ARCHIVE_MAP: Any
OPENAI_GPT_PRETRAINED_CONFIG_ARCHIVE_MAP: Any

def load_tf_weights_in_openai_gpt(model: Any, config: Any, openai_checkpoint_folder_path: Any): ...
def gelu(x: Any): ...
def swish(x: Any): ...

ACT_FNS: Any

class OpenAIGPTConfig(PretrainedConfig):
    pretrained_config_archive_map: Any = ...
    vocab_size: Any = ...
    n_ctx: Any = ...
    n_positions: Any = ...
    n_embd: Any = ...
    n_layer: Any = ...
    n_head: Any = ...
    afn: Any = ...
    resid_pdrop: Any = ...
    embd_pdrop: Any = ...
    attn_pdrop: Any = ...
    layer_norm_epsilon: Any = ...
    initializer_range: Any = ...
    predict_special_tokens: Any = ...
    num_labels: Any = ...
    summary_type: Any = ...
    summary_use_proj: Any = ...
    summary_activation: Any = ...
    summary_first_dropout: Any = ...
    summary_proj_to_labels: Any = ...
    def __init__(self, vocab_size_or_config_json_file: int = ..., n_positions: int = ..., n_ctx: int = ..., n_embd: int = ..., n_layer: int = ..., n_head: int = ..., afn: str = ..., resid_pdrop: float = ..., embd_pdrop: float = ..., attn_pdrop: float = ..., layer_norm_epsilon: float = ..., initializer_range: float = ..., predict_special_tokens: bool = ..., num_labels: int = ..., summary_type: str = ..., summary_use_proj: bool = ..., summary_activation: Optional[Any] = ..., summary_proj_to_labels: bool = ..., summary_first_dropout: float = ..., **kwargs: Any) -> None: ...
    @property
    def max_position_embeddings(self): ...
    @property
    def hidden_size(self): ...
    @property
    def num_attention_heads(self): ...
    @property
    def num_hidden_layers(self): ...

class Attention(nn.Module):
    n_head: Any = ...
    split_size: Any = ...
    scale: Any = ...
    output_attentions: Any = ...
    c_attn: Any = ...
    c_proj: Any = ...
    attn_dropout: Any = ...
    resid_dropout: Any = ...
    def __init__(self, nx: Any, n_ctx: Any, config: Any, scale: bool = ...) -> None: ...
    def prune_heads(self, heads: Any) -> None: ...
    def merge_heads(self, x: Any): ...
    def split_heads(self, x: Any, k: bool = ...): ...
    def forward(self, x: Any, head_mask: Optional[Any] = ...): ...

class MLP(nn.Module):
    c_fc: Any = ...
    c_proj: Any = ...
    act: Any = ...
    dropout: Any = ...
    def __init__(self, n_state: Any, config: Any) -> None: ...
    def forward(self, x: Any): ...

class Block(nn.Module):
    attn: Any = ...
    ln_1: Any = ...
    mlp: Any = ...
    ln_2: Any = ...
    def __init__(self, n_ctx: Any, config: Any, scale: bool = ...) -> None: ...
    def forward(self, x: Any, head_mask: Optional[Any] = ...): ...

class OpenAIGPTPreTrainedModel(PreTrainedModel):
    config_class: Any = ...
    pretrained_model_archive_map: Any = ...
    load_tf_weights: Any = ...
    base_model_prefix: str = ...
    def __init__(self, *inputs: Any, **kwargs: Any) -> None: ...
    def init_weights(self, module: Any) -> None: ...

OPENAI_GPT_START_DOCSTRING: str
OPENAI_GPT_INPUTS_DOCSTRING: str

class OpenAIGPTModel(OpenAIGPTPreTrainedModel):
    output_attentions: Any = ...
    output_hidden_states: Any = ...
    tokens_embed: Any = ...
    positions_embed: Any = ...
    drop: Any = ...
    h: Any = ...
    def __init__(self, config: Any) -> None: ...
    def forward(self, input_ids: Any, position_ids: Optional[Any] = ..., token_type_ids: Optional[Any] = ..., head_mask: Optional[Any] = ...): ...

class OpenAIGPTLMHeadModel(OpenAIGPTPreTrainedModel):
    transformer: Any = ...
    lm_head: Any = ...
    def __init__(self, config: Any) -> None: ...
    def tie_weights(self) -> None: ...
    def forward(self, input_ids: Any, position_ids: Optional[Any] = ..., token_type_ids: Optional[Any] = ..., labels: Optional[Any] = ..., head_mask: Optional[Any] = ...): ...

class OpenAIGPTDoubleHeadsModel(OpenAIGPTPreTrainedModel):
    transformer: Any = ...
    lm_head: Any = ...
    multiple_choice_head: Any = ...
    def __init__(self, config: Any) -> None: ...
    def tie_weights(self) -> None: ...
    def forward(self, input_ids: Any, mc_token_ids: Optional[Any] = ..., lm_labels: Optional[Any] = ..., mc_labels: Optional[Any] = ..., token_type_ids: Optional[Any] = ..., position_ids: Optional[Any] = ..., head_mask: Optional[Any] = ...): ...