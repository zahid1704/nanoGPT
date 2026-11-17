# nanoGPT
This repository holds the source code for a Generative Pre-trained Transformer (GPT), which is a language model built on the Transformer architecture. GPT is a state-of-the-art language model architecture that delivers remarkable performance across a wide range of natural language processing tasks, such as understanding language and generating text. This project features a compact, scaled-down version of the GPT architecture containing around 10.8 million parameters, mirroring the structure of standard Large Language Models, but generates characters not subwords. While heavily inspired by Andrej Karpathy's educational GPT walkthrough, every line of code was implemented independently from scratch and trained iteratively on the Shakespeare dataset. Hyperparameters and custom optimizers were systematically tuned by monitoring training and validation losses to achieve optimal performance.

Some of the training results and adjustments are discussed below. 

# Phase 1:
AdamW Optimizer; \
Learning Rate: 1e-3; \
Dropout: 0.2

![first training output](assets/trainingVSvalidationLoss01.png)

The graph indicates that the model initially learned effectively before performance gradually degraded, signaling that an excessively high learning rate caused the optimization to overshoot the gradient descent minima. To address this, both the learning rate and dropout rate were lowered for the subsequent training phase.


# Phase 2: 
AdamW Optimizer; \
Learning Rate: 3e-4; \
Dropout: 0.05

![second training output](assets/trainingVSvalidationLoss02.png)

Although the second test successfully lowered the training loss, the validation loss continued to climb after an initial improvement, causing a widening gap between the two curves—a classic phenomenon of overfitting. To counter this, only the dropout rate was increased for the next phase to improve generalization.


# Phase 3: 
AdamW Optimizer; \
Learning Rate: 3e-4; \
Dropout: 0.15

![third training output](assets/trainingVSvalidationLoss03.png)

During this phase, both training and validation losses successfully decreased to optimal levels, with validation loss only ticking up slightly in the final few iterations. This indicated that the learning rate and dropout were well-tuned, so a cosine learning rate scheduler was introduced for the final stage to smooth out the end-of-training anomaly and achieve even better results.


# Phase 4:
AdamW Optimizer; \
Learning Rate: 3e-4; \
Dropout: 0.15; \
a new optimizer "cosine learning rate scheduler" is added.

![forth training output](assets/trainingVSvalidationLoss04.png)

This phase delivered the best results among first 4, with both training and validation losses steadily plummeting throughout the entire training process until both reached optimal levels.

# Phase 5: 
AdamW Optimizer; \
Learning Rate: 3e-4; \
Dropout: 0.2; \
Cosine Learning Rate Scheduler

![fifth training output](assets/trainingVSvalidationLoss05.png)

During this phase, the gap between training and validation loss narrowed noticeably. Raising the dropout rate to 0.2 prevented the model from merely memorizing the training set, enabling it to generalize more effectively across the dataset.

# Final Verdict: 
A comparison between the two top-performing stages (Phase 4 and Phase 5) reveals that the latter achieved superior overall performance. While both demonstrated a steady decline in training and validation losses, Phase 5 maintained a narrower and more stable margin between the two curves. In contrast, Phase 4 exhibited a much sharper, more pronounced divergence.


![GeneralizationGapPhase4vsPhase5 output](assets/GeneralizationGapPhase4vsPhase5.png)

# Loss Curve on each step of Phase 5:
AdamW Optimizer; \
Learning Rate: 3e-4; \
Dropout: 0.2; \
Cosine Learning Rate Scheduler \
Training and Validation Data Ratio (train:val) = (9:1) \
50000 Steps of training

![Loss_Curve_Each_Step_Phase05 output](assets/Loss_Curve_Each_Step_Phase05.png)

\
# Trying Different New Dataset
Retaining the identical hyperparameters from Phase 5 of the Tiny Shakespeare training, scaling the nanoGPT model to the TinyStories dataset yielded exceptional results. Throughout the training cycle, the training and validation loss curves tracked one another almost identically, resulting in a near-zero generalization gap and a complete absence of overfitting.
![LossOnCurveOntrainingVSvalidationLossTinyStories output](assets/trainingVSvalidationLoss_TinyStories.png)



Comparing the training-versus-validation loss gap between the Tiny Shakespeare (Phase 5) and TinyStories runs reveals that TinyStories achieves a virtually zero generalization gap, with both loss curves running completely parallel. This demonstrates that the hyperparameter configuration established in the previous phase was fundamentally optimal, allowing the model to effectively generalize data patterns when provided with sufficient training scale.

![GeneralizationGapShakespeare_vs_TinyStories_output](assets/GeneralizationGapShakespeare_vs_TinyStories.png)

# Loss Curve on each step of TinyStories:
AdamW Optimizer; \
Learning Rate: 3e-4; \
Dropout: 0.2; \
Cosine Learning Rate Scheduler \
Training and Validation Data Ratio (train:val) = (9:1) => (400K:40K) stories \
50000 Steps of training

![LossCurveOnEachStepOfTinyStories_output](assets/LossCurveOnEachStepOfTinyStories.png)



