### input preparation stage

1. text preparation: `string` -> `list[int]` (token ids)
2. token embedding: `list[int]` -> `tensor[sequence length, hidden dimension]`
3. positional encoding: `tensor[sequence length, hidden dimension]` -> `tensor[sequence length, hidden dimension]`

### core transformer block

1. multi-head attention layer: `tensor[sequence length, hidden dimension]` -> `tensor[sequence length, hidden dimension]`
2. feed forward network: `tensor[sequence length, hidden dimension]` -> `tensor[sequence length, hidden dimension]`
3. normalization and residual components: `tensor[sequence length, hidden dimension]` -> `tensor[sequence length, hidden dimension]`

### efficiency and generation upgrades

1. causal attention masking matrix: `tensor[sequence length, sequence length]` (mask) + `tensor` (pre-softmax scores) -> `tensor` (masked scores)
2. kv cache manager: `tensor` (new key/value) + `tensor` (cached key/value) -> `tensor` (updated key/value history)

### prediction head

1. language model head: `tensor[sequence length, hidden dimension]` -> `tensor[sequence length, vocabulary size]` (logits)
2. sampler component: `tensor[vocabulary size]` (logits) -> `int` (next token id)
