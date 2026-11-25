import numpy as np

class Vector :
        def __init__(self,values):
            self.values = np.array(values,dtype=float)
        
        def __repr__(self):
            return f"Vector({self.values})"
        
        def __len__(self):
            return len(self.values)
        
        def __getitem__(self,index):
            return self.values[index]
        
        def __setitem__(self,index,value):
            self.values[index]=value
        
        def __add__(self, other):
            return Vector(self.values+other.values)
        
        def __sub__(self,other):
            return Vector(self.values - other.values)
        
        def __mul__(self,scalar):
            return Vector(self.values * scalar)
        
        def __rmul__(self,scalar):
            return Vector(scalar * self.values)
        
        def __imul__(self,scalar):
            self.values *= scalar
            return self
        def dot(self,other):
            return np.dot(self.values,other.values)
        
        def magnitude(self):
            return np.linalg.norm(self.values)
        
        def l2_norm(self):
            return Vector(self.values/np.linalg.norm(self.values))
        

class Neural_utils:

        @staticmethod
        def dense(X,W,b):
            return np.dot(X,W)+b
        
        @staticmethod
        def layernorm(X,gamma,beta, eps=1e-5):
            mean = np.mean(X)
            var = np.var(X)

            return gamma*((X-mean)/(np.sqrt(var+eps)))+beta
        
        @staticmethod
        def relu(X):
            return np.maximum(X,0)
        
        @staticmethod
        def leaky_relu(X,alpha = 0.01):
            return np.where(X>0,X,X*alpha)
        
        @staticmethod
        def softmax(X):
            exp = np.exp(X-np.max(X))
            return exp/np.sum(exp)
        
        @staticmethod
        def onehotencoding(index,num_classes):
            vec = np.zeros(num_classes)
            vec[index]=1
            return vec
        
        @staticmethod
        def mean(x):
            return np.mean(x)
        
        @staticmethod
        def standard_deviation(x):
            return np.std(x)
        
        @staticmethod
        def l2_normalize(x):
            return x/np.linalg.norm(x)
        
        @staticmethod
        def gelu(X):
            return 0.5*X*(1+np.tanh(np.sqrt(2/np.pi)*(X+(0.044715*X**3))))
        


if __name__ == "__main__":
        # ==============================
        # VECTOR CLASS TESTING
        # ==============================

        v1 = Vector([1, 2, 3])
        v2 = Vector([4, 5, 6])

        print("---- VECTOR TESTING ----")

        # Test representation
        print("Vector 1:", repr(v1))

        # Test length
        print("Length:", len(v1))

        # Test getitem
        print("Element at index 1:", v1[1])

        # Test setitem
        v1[0] = 10
        print("After setting index 0:", v1.values)

        # Test addition
        print("Addition:", (v1 + v2).values)

        # Test subtraction
        print("Subtraction:", (v2 - v1).values)

        # Test multiplication
        print("Multiplication:", (v1 * 2).values)

        # Test reverse multiplication
        print("Reverse multiplication:", (3 * v1).values)

        # Test inplace multiplication
        v3 = Vector([1, 2, 3])
        v3 *= 2
        print("Inplace multiplication:", v3.values)

        # Test dot product
        print("Dot product:", v1.dot(v2))

        # Test magnitude
        print("Magnitude:", v1.magnitude())

        # Test L2 norm
        print("L2 norm:", v1.l2_norm().values)


        # ==============================
        # NEURAL_UTILS CLASS TESTING
        # ==============================

        print("\n---- NEURAL UTILS TESTING ----")

        # Test dense layer
        X = np.array([[1, 2]])
        W = np.array([[3, 4], [5, 6]])
        b = np.array([1, 1])

        print("Dense:", Neural_utils.dense(X, W, b))

        # Test layer normalization
        X = np.array([1.0, 2.0, 3.0])
        gamma = 1.0
        beta = 0.0

        print("LayerNorm:", Neural_utils.layernorm(X, gamma, beta))

        # Test ReLU
        X = np.array([-2, -1, 0, 1, 2])
        print("ReLU:", Neural_utils.relu(X))

        # Test Leaky ReLU
        print("Leaky ReLU:", Neural_utils.leaky_relu(X))

        # Test Softmax
        X = np.array([1.0, 2.0, 3.0])
        print("Softmax:", Neural_utils.softmax(X))

        # Test One Hot Encoding
        print("One Hot Encoding:", Neural_utils.onehotencoding(2, 5))

        # Test Mean
        X = np.array([1, 2, 3, 4, 5])
        print("Mean:", Neural_utils.mean(X))

        # Test Standard Deviation
        print("Standard Deviation:", Neural_utils.standard_deviation(X))

        # Test L2 Normalization
        X = np.array([3.0, 4.0])
        print("L2 Normalize:", Neural_utils.l2_normalize(X))

        # Test GELU
        X = np.array([-2.0, -1.0, 0.0, 1.0, 2.0])
        print("GELU:", Neural_utils.gelu(X))

        print("\n\n ALL THE TEST CASES PASSED")