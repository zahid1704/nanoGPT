import torch

# Device configaration

def get_device():
  if torch.cuda.is_available():
    device = torch.device('cuda')
    print(f"Using Nvidia GPU: {torch.cuda.get_device_name(0)}")
  elif torch.backends.mps.is_available():
    device = torch.device('mps')
    print("Using Apple Silicon GPU")
  else:
    device = torch.device('cpu')
    print("Using CPU. (Warning: Execution might be slow..)")
  return device


# Hyperparameters

device = get_device()
batch_size = 64 # number of independent sequences that will be processed in parallel.
block_size = 256 # the maximum context length for predictions.
max_iters = 5000
eval_interval = 500
learning_rate = 3e-4
eval_iters = 200
n_embd = 384
n_head = 6
n_layer = 6
dropout = 0.2
torch.manual_seed(1337)
