

!pip install datasets
from datasets import load_dataset
import torch
import itertools


# Loading Dataset"

!pip install datasets
from datasets import load_dataset

train_dataset = load_dataset("roneneldan/TinyStories", split="train[:400000]")
validation_dataset = load_dataset("roneneldan/TinyStories", split="validation[:40000]")

# Bring object data to text list
train_text = '\n\n'.join(train_dataset['text'])
validation_text = '\n\n'.join(validation_dataset['text'])

# Creating set of unique characters from both datasets.
unique_chars = set()
for uch in itertools.chain(train_text, validation_text):
  unique_chars.update(uch)

chars = sorted(list(unique_chars))
vocab_size = len(chars)

# Creating a Mapping
stoi = { ch:i for i,ch in enumerate(chars) } # Create a dictionary Key=Character, Value=corresponding Number
itos = { i:ch for i,ch in enumerate(chars) } # Create a dictionary Key=Number, Value=corresponding Character
encode = lambda s: [stoi[c] for c in s]   # Take characters and convert to integers
decode = lambda l: ''.join([itos[i] for i in l]) # Take integers and convert to Characters

# Encoding Entire dataset of shakespear and store is torch.Tensor
train_data = torch.tensor(encode(train_text), dtype=torch.long)

validation_data = torch.tensor(encode(validation_text), dtype=torch.long)

# data loading
def get_batch(split):
    # generate a small batch of data of inputs x and targets y
    data = train_data if split == 'train' else validation_data
    ix = torch.randint(len(data) - block_size, (batch_size,))
    x = torch.stack([data[i:i+block_size] for i in ix]) # Here x is (block_size*batch_size) tensor
    y = torch.stack([data[i+1:i+block_size+1] for i in ix]) # Here y is (block_size*batch_size) tensor
    x, y = x.to(device), y.to(device)
    return x, y