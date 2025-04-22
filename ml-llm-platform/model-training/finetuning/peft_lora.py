# Contents of the file: /ml-llm-platform/ml-llm-platform/model-training/finetuning/peft_lora.py

import torch
from torch import nn
from transformers import AutoModelForSequenceClassification, AutoTokenizer

class LoRA(nn.Module):
    def __init__(self, model_name, rank=8):
        super(LoRA, self).__init__()
        self.model = AutoModelForSequenceClassification.from_pretrained(model_name)
        self.rank = rank
        self.lora_layers = self._add_lora_layers()

    def _add_lora_layers(self):
        lora_layers = {}
        for name, param in self.model.named_parameters():
            if 'weight' in name:
                lora_layer = nn.Parameter(torch.zeros_like(param))
                lora_layers[name] = lora_layer
                self.register_parameter(name + '_lora', lora_layer)
        return lora_layers

    def forward(self, input_ids, attention_mask, labels):
        outputs = self.model(input_ids, attention_mask=attention_mask, labels=labels)
        loss = outputs.loss
        logits = outputs.logits

        for name, lora_layer in self.lora_layers.items():
            if name in self.model.named_parameters():
                self.model.named_parameters()[name].data += lora_layer.data

        return loss, logits

def fine_tune_model(model_name, train_dataset, val_dataset, epochs=3, learning_rate=5e-5):
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = LoRA(model_name)

    optimizer = torch.optim.AdamW(model.parameters(), lr=learning_rate)

    for epoch in range(epochs):
        model.train()
        for batch in train_dataset:
            optimizer.zero_grad()
            input_ids = tokenizer(batch['text'], return_tensors='pt', padding=True, truncation=True).input_ids
            attention_mask = tokenizer(batch['text'], return_tensors='pt', padding=True, truncation=True).attention_mask
            labels = batch['labels']

            loss, _ = model(input_ids, attention_mask, labels)
            loss.backward()
            optimizer.step()

        print(f'Epoch {epoch + 1}/{epochs} completed.')

    return model

# Example usage
# model = fine_tune_model('bert-base-uncased', train_dataset, val_dataset)