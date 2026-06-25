import numpy as np
def sigmoid(x):  return 1 / (1 + np.exp(-x))
def sigmoid_d(x):  return x * (1 - x)

#XOR Problem - A Simple Neural Network test:-
X = np.array([[0,0],[0,1],[1,0],[1,1]])
y = np.array([[0],[1],[1],[0]])

np.random.seed(42)
w1 = np.random.randn(2,4) * 0.5
w2 = np.random.randn(4,1) * 0.5

lr = 0.5             #Learning Rate
losses = []

for each in range(10000):
    #Forward Pass:-
    h = sigmoid(X @ w1)
    o = sigmoid(h @ w2)
    
    #Loss (Mean Squared Error):-
    loss = np.mean((y - o)**2)
    losses.append(loss)
    
    #Backward Pass - Compute Gradients:-
    d_o = (o-y)* sigmoid_d(o)
    d_h = (d_o @ w2.T) * sigmoid_d(h)
    
    #Update Weights:-
    w2 -= lr * h.T @ d_o
    w1 -= lr * X.T @ d_h
    
import matplotlib.pyplot as plt 
plt.plot(losses); plt.title('Loss Decreasing During Training')
plt.xlabel('Epoch'); plt.ylabel('Loss'); plt.show()

print('Final predictions (should be close to [0,1,1,0]):')
print(np.random(0, 2))         