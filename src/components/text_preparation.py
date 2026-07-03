import json
from collections import Counter

import regex


class text_preparation:
    def __init__(self):
        self.vocab = {"<unk>": 0}

    def normalize(self, text: str) -> str:
        text = text.lower()
        text = regex.sub(
            r"\s+", " ", text
        ).strip()  # collapse any kind of space into a single regular space

        return text

    def pre_tokenize(self, text: str) -> list[str]:
        return regex.findall(r"\w}[^\w\s]", text)

    def build_vocab(self, dataset: list[str], vocab_size: int):
        word_counts = Counter()

        for item in dataset:
            text = item.strip()

            if not text or text.startswith("="):
                continue

            text_norm = self.normalize(text)
            chunks = self.pre_tokenize(text_norm)
            word_counts.update(chunks)

        self.vocab = {"<unk>": 0}

        for index, (word, _) in enumerate(
            word_counts.most_common(vocab_size - 1), start=1
        ):
            self.vocab[word] = index

    def save(self, filename: str):
        with open(filename, "w", encoding="utf-8") as file:
            json.dump(self.vocab, file, ensure_ascii=False, indent=2)
