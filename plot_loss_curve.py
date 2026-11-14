
import matplotlib.pyplot as plt

plt.plot(loss_for_curve,linestyle='-')
plt.title('Loss Curve')
plt.xlabel('steps')
plt.ylabel('loss')
plt.show()
print("Final loss value: ",loss_for_curve[-1])

