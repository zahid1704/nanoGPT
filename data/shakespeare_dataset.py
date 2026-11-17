

# Importing packages

import requests
import os
import torch


# Loading Dataset
try:
  base_dir = os.path.dirname(os.path.abspath(__file__))
except NameError:
  base_dir = os.getcwd()

input_file_path = os.path.join(base_dir, 'input.txt')
if not os.path.exists(input_file_path):
    data_url = 'https://raw.githubusercontent.com/karpathy/char-rnn/master/data/tinyshakespeare/input.txt'
    with open(input_file_path, 'w') as f:
        f.write(requests.get(data_url).text)

with open(input_file_path, 'r', encoding='utf-8') as f:
  text = f.read()


#Extract All unique characters in the Dataset, make a sorted list, take length
chars = sorted(list(set(text)))
vocab_size = len(chars)


#Creating a Mapping
stoi = { ch:i for i,ch in enumerate(chars) } # Create a dictionary Key=Character, Value=corresponding Number
itos = { i:ch for i,ch in enumerate(chars) } # Create a dictionary Key=Number, Value=corresponding Character
encode = lambda s: [stoi[c] for c in s]   # Take characters and convert to integers
decode = lambda l: ''.join([itos[i] for i in l]) # Take integers and convert to Characters


#Encoding Entire dataset of shakespear and store is torch.Tensor
data = torch.tensor(encode(text), dtype=torch.long)


# Spliting training and validation dataset
n = int(0.9*len(data))
train_data = data[:n] # First 90% is training data
val_data = data[n:] # Last 10% is validation data



# data loading
def get_batch(split):
    # generate a small batch of data of inputs x and targets y
    data = train_data if split == 'train' else val_data
    ix = torch.randint(len(data) - block_size, (batch_size,))
    x = torch.stack([data[i:i+block_size] for i in ix]) # Here x is (block_size*batch_size) tensor
    y = torch.stack([data[i+1:i+block_size+1] for i in ix]) # Here y is (block_size*batch_size) tensor
    x, y = x.to(device), y.to(device)
    return x, y

