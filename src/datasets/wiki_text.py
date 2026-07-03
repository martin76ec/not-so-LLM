from datasets import load_dataset


def wikitext_get():
    dataset = load_dataset("wikitext", name="wikitext-2-raw-v1", split="train")
    __import__("pdb").set_trace()
