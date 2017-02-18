"""Softmax."""

scores = [3.0, 1.0, 0.2]
import numpy as np

def softmax(x):
    """Compute softmax values for each sets of scores in x."""
    return np.exp(x)/ np.sum(np.exp(x), axis=0)

print(softmax(scores))

# Plot softmax curves
import matplotlib.pyplot as plt
x = np.arange(-2.0, 6.0, 0.1)
scores = np.vstack([x, np.ones_like(x), 0.2 * np.ones_like(x)])
plt.plot(x, softmax(scores).T, linewidth=2)
plt.ylabel('Scores')
plt.xlabel('Values')
plt.title('Softmax Score Example')
plt.legend(['x','1.0','0.2'])
plt.show()


#Test
scores = [1.0, 2.0, 3.0]
print(softmax(scores)) #[ 0.09003057  0.24472847  0.66524096]
scores = np.array([[1, 2, 3, 6], [2, 4, 5, 6], [3, 8, 7, 6]])
print(softmax(scores))
#[[ 0.09003057  0.00242826  0.01587624  0.33333333]
# [ 0.24472847  0.01794253  0.11731043  0.33333333]
# [ 0.66524096  0.97962921  0.86681333  0.33333333]]

# When values of y are large ,
# the values of the softmax  are closer to 0 and 1 (more confident)
scores = [x*10 for x in [1.0, 2.0, 3.0]]
print(softmax(scores)) #[  2.06106005e-09   4.53978686e-05   9.99954600e-01]
# When values of y are small ,
# the values of the softmax approaches that of a uniform distribution (less confident)
scores = [x/10 for x in [1.0, 2.0, 3.0]]
print(softmax(scores)) #[ 0.30060961  0.33222499  0.3671654 ]

num_classes = 10
np.random.seed(133)


