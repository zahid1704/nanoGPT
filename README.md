# nanoGPT
This repository holds the source code for a Generative Pre-trained Transformer (GPT), which is a language model built on the Transformer architecture. GPT is a state-of-the-art language model architecture hat delivers remarkable performance across a wide range of natural language processing tasks, such as understanding language and generating text. This project features a compact, scaled-down version of the GPT architecture containing around 10.8 million parameters, mirroring the structure of standard Large Language Models. While heavily inspired by Andrej Karpathy's educational GPT walkthrough, every line of code was implemented independently from scratch and trained iteratively on the Shakespeare dataset. Hyperparameters and custom optimizers were systematically tuned by monitoring training and validation losses to achieve optimal performance.

Some of the training results and adjustments are discussed below. 

# Phase 1:
AdamW Optimizer
Learning Rate: 1e-3
Dropout: 0.2
![first training output](assets/trainingVSvalidationLoss01.png)
The graph indicates that the model initially learned effectively before performance gradually degraded, signaling that an excessively high learning rate caused the optimization to overshoot the gradient descent minima. To address this, both the learning rate and dropout rate were lowered for the subsequent training phase.
