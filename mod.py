from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch

class mod:
    def __init__(self):
        self.tokenizer = AutoTokenizer.from_pretrained('facebook/roberta-hate-speech-dynabench-r4-target')
        self.model = AutoModelForSequenceClassification.from_pretrained(
            'facebook/roberta-hate-speech-dynabench-r4-target')

    def check(self, message) -> int:
        tokens = self.tokenizer.encode(message, return_tensors='pt')
        result = int(torch.argmax((self.model(tokens)).logits))
        return result
