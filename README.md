Token — Summary
A token is the smallest unit of text that an LLM processes.
Tokens are not always words. A word can be:
1 token (cat)
Multiple tokens (playing → play + ing)
Punctuation and spaces can also be separate tokens.
Before the model reads your prompt, a tokenizer converts text into token IDs (numbers).
The LLM works with these numbers, not raw text.
After generating token IDs, the tokenizer converts them back into readable text.


PIPELINE

Your Text
    ↓
Tokenizer
    ↓
Tokens
    ↓
Token IDs (numbers)
    ↓
LLM
    ↓
Predicted Token IDs
    ↓
Tokenizer
    ↓
Readable Text

In simple words , A token is the basic unit of text an LLM understands and generates. It is converted into a numeric ID before a
the model processes it.
