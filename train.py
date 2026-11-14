

import torch.optim as optim


m = GPTLanguageModel()
model = m.to(device)

# number of parameters in the model
print(sum(p.numel() for p in model.parameters())/1e6, 'million parameters')

optimizer = optim.AdamW(model.parameters(), lr=learning_rate)

# Add the Cosine Annealing Scheduler, eta_min is the minimum learning rate it will decay down to (10% of peak is standard)
scheduler = optim.lr_scheduler.CosineAnnealingLR(
    optimizer,
    T_max=max_iters,
    eta_min=learning_rate * 0.1
)


# evaluate loss
loss_for_curve=[]
for iter in range(max_iters):

  if iter % eval_interval == 0 or iter == max_iters - 1:
    losses = estimate_loss()
    print(f"step {iter}: train loss {losses['train']:.4f}, val loss {losses['val']:.4f}")

  # sample a batch of data
  xb, yb = get_batch('train')


  logits, loss = model(xb, yb)
  optimizer.zero_grad(set_to_none=True)
  loss.backward()
  optimizer.step()
  scheduler.step()
  loss_for_curve.append(loss.item())
